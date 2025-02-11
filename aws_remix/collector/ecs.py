import boto3
import datetime

def collect_ecs_info_with_utilization(region, days=14):
    """
    Enhanced ECS collector that:
      1) Lists ECS clusters and their services.
      2) For each service, retrieves detailed information and
         gathers CloudWatch metrics for CPUUtilization and MemoryUtilization.
    Returns a list of clusters, each with a list of service details and utilization metrics.
    """
    ecs_client = boto3.client('ecs', region_name=region)
    cw_client = boto3.client('cloudwatch', region_name=region)
    clusters_info = []
    try:
        clusters_response = ecs_client.list_clusters()
        cluster_arns = clusters_response.get("clusterArns", [])
        for cluster_arn in cluster_arns:
            # Extract the cluster name from the ARN (assumes the ARN ends with the cluster name)
            cluster_name = cluster_arn.split("/")[-1]
            
            # List services in this cluster
            services_response = ecs_client.list_services(cluster=cluster_arn)
            service_arns = services_response.get("serviceArns", [])
            services_details = []
            if service_arns:
                # Describe services to get more detailed info
                describe_response = ecs_client.describe_services(cluster=cluster_arn, services=service_arns)
                for service in describe_response.get("services", []):
                    service_name = service.get("serviceName")
                    service_detail = {
                        "ServiceName": service_name,
                        "ServiceArn": service.get("serviceArn"),
                        "DesiredCount": service.get("desiredCount"),
                        "RunningCount": service.get("runningCount"),
                        "PendingCount": service.get("pendingCount"),
                        "Utilization": {}
                    }
                    # Prepare dimensions for CloudWatch metrics (using both ClusterName and ServiceName)
                    dimensions = [
                        {"Name": "ClusterName", "Value": cluster_name},
                        {"Name": "ServiceName", "Value": service_name}
                    ]
                    cpu_data = _get_daily_metric_stats_multi(
                        cw_client,
                        namespace="AWS/ECS",
                        metric_name="CPUUtilization",
                        dimensions=dimensions,
                        days=days,
                        stat="Average",
                        unit="Percent"
                    )
                    mem_data = _get_daily_metric_stats_multi(
                        cw_client,
                        namespace="AWS/ECS",
                        metric_name="MemoryUtilization",
                        dimensions=dimensions,
                        days=days,
                        stat="Average",
                        unit="Percent"
                    )
                    service_detail["Utilization"]["CPU"] = cpu_data
                    service_detail["Utilization"]["Memory"] = mem_data
                    services_details.append(service_detail)
                    
            clusters_info.append({
                "ClusterArn": cluster_arn,
                "ClusterName": cluster_name,
                "Services": services_details
            })
    except Exception as e:
        clusters_info.append({"error": str(e)})

    return clusters_info


def _get_daily_metric_stats_multi(
    cw_client,
    namespace,
    metric_name,
    dimensions,
    days=14,
    stat="Average",
    unit=None
):
    """
    Helper to fetch daily metric statistics for a given metric with multiple dimensions.
    Returns a list of dictionaries: [ { "Timestamp": ..., stat: value }, ... ]
    """
    end_time = datetime.datetime.utcnow()
    start_time = end_time - datetime.timedelta(days=days)
    period = 86400  # one datapoint per day

    metrics_data = []
    try:
        response = cw_client.get_metric_statistics(
            Namespace=namespace,
            MetricName=metric_name,
            Dimensions=dimensions,
            StartTime=start_time,
            EndTime=end_time,
            Period=period,
            Statistics=[stat],
            Unit=unit if unit else None
        )
        datapoints = response.get("Datapoints", [])
        datapoints.sort(key=lambda x: x["Timestamp"])
        for dp in datapoints:
            value = dp.get(stat, 0.0)
            timestamp = dp["Timestamp"].isoformat()
            metrics_data.append({
                "Timestamp": timestamp,
                stat: value
            })
    except Exception as e:
        metrics_data.append({"error": str(e)})

    return metrics_data
