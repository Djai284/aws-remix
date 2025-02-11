import boto3
import datetime

# List old-generation instance families for modernization checks
OLD_GENERATION_FAMILIES = [
    "m1", "m2", "m3", "m4",
    "c1", "c3", "c4",
    "t1", "t2",
    "r3", "r4",
    "i2",
    "g2",
    # Add others as needed...
]

def collect_ec2_info_with_utilization(region, days=14):
    """
    Enhanced collector that:
      1) Lists EC2 instances with detailed configuration (instance type, state, launch time, etc.)
         and EBS volume details.
      2) Gathers CloudWatch metrics for CPU and network usage over the last `days`.
      3) For each attached EBS volume, collects utilization metrics such as read/write ops and bytes.
    Returns a list of dictionaries, one per instance.
    """
    ec2_client = boto3.client('ec2', region_name=region)
    cw_client = boto3.client('cloudwatch', region_name=region)

    instances = []
    try:
        response = ec2_client.describe_instances()
        for reservation in response.get("Reservations", []):
            for instance in reservation.get("Instances", []):
                instance_id = instance.get("InstanceId")
                instance_type = instance.get("InstanceType")
                
                instance_data = {
                    "InstanceId": instance_id,
                    "InstanceType": instance_type,
                    "State": instance.get("State", {}).get("Name"),
                    "LaunchTime": str(instance.get("LaunchTime")),
                    "Pillars": ["Reliability", "PerformanceEfficiency", "CostOptimization"],
                    "IsOldGeneration": _is_old_generation(instance_type),
                    "PrivateIpAddress": instance.get("PrivateIpAddress"),
                    "PublicIpAddress": instance.get("PublicIpAddress"),
                    "KeyName": instance.get("KeyName"),
                    "SecurityGroups": [],
                    "Tags": [],
                    "EBSVolumes": [],
                    "Utilization": {
                        "CPU": [],         # daily CPU datapoints
                        "NetworkIn": [],   # daily average
                        "NetworkOut": []   # daily average
                    }
                }

                # 1a. Collect Security Groups
                for sg in instance.get("SecurityGroups", []):
                    instance_data["SecurityGroups"].append({
                        "GroupId": sg.get("GroupId"),
                        "GroupName": sg.get("GroupName")
                    })

                # 1b. Collect Tags
                for tag in instance.get("Tags", []):
                    instance_data["Tags"].append({
                        "Key": tag.get("Key"),
                        "Value": tag.get("Value")
                    })

                # 1c. Collect EBS volume details and utilization metrics
                block_devices = instance.get("BlockDeviceMappings", [])
                for bd in block_devices:
                    ebs = bd.get("Ebs", {})
                    if "VolumeId" in ebs:
                        vol_data = _describe_ebs_volume(ec2_client, ebs["VolumeId"], cw_client=cw_client, days=days)
                        instance_data["EBSVolumes"].append(vol_data)

                # 2. Collect CloudWatch metrics for EC2 instance
                cpu_data = _get_daily_metric_stats(
                    cw_client,
                    namespace="AWS/EC2",
                    metric_name="CPUUtilization",
                    dimension_name="InstanceId",
                    dimension_value=instance_id,
                    days=days,
                    stat="Average",
                    unit="Percent"
                )
                instance_data["Utilization"]["CPU"] = cpu_data

                net_in_data = _get_daily_metric_stats(
                    cw_client,
                    namespace="AWS/EC2",
                    metric_name="NetworkIn",
                    dimension_name="InstanceId",
                    dimension_value=instance_id,
                    days=days,
                    stat="Average",
                    unit="Bytes"
                )
                instance_data["Utilization"]["NetworkIn"] = net_in_data

                net_out_data = _get_daily_metric_stats(
                    cw_client,
                    namespace="AWS/EC2",
                    metric_name="NetworkOut",
                    dimension_name="InstanceId",
                    dimension_value=instance_id,
                    days=days,
                    stat="Average",
                    unit="Bytes"
                )
                instance_data["Utilization"]["NetworkOut"] = net_out_data

                instances.append(instance_data)

    except Exception as e:
        instances.append({"error": str(e)})

    return instances


def _is_old_generation(instance_type):
    """
    Returns True if 'instance_type' belongs to an older-generation family.
    """
    if not instance_type:
        return False
    family_prefix = instance_type.split(".")[0]
    return family_prefix in OLD_GENERATION_FAMILIES


def _describe_ebs_volume(ec2_client, volume_id, cw_client=None, days=14):
    """
    Helper function to get more details on an EBS volume:
      - Basic properties: VolumeId, Encrypted, VolumeType, Iops, Throughput, SizeGiB.
      - If a CloudWatch client is provided, also collects utilization metrics:
          - VolumeReadOps, VolumeWriteOps, VolumeReadBytes, VolumeWriteBytes.
    """
    vol_data = {
        "VolumeId": volume_id,
        "Encrypted": False,
        "VolumeType": None,
        "Iops": None,
        "Throughput": None,
        "SizeGiB": None
    }

    try:
        resp = ec2_client.describe_volumes(VolumeIds=[volume_id])
        volumes = resp.get("Volumes", [])
        if volumes:
            v = volumes[0]
            vol_data["Encrypted"] = v.get("Encrypted", False)
            vol_data["VolumeType"] = v.get("VolumeType")
            vol_data["Iops"] = v.get("Iops")
            vol_data["Throughput"] = v.get("Throughput")
            vol_data["SizeGiB"] = v.get("Size")
    except Exception as e:
        vol_data["error"] = str(e)

    # If a CloudWatch client is provided, add utilization metrics
    if cw_client:
        utilization = {}
        metrics = {
            "VolumeReadOps": {"stat": "Sum", "unit": "Count"},
            "VolumeWriteOps": {"stat": "Sum", "unit": "Count"},
            "VolumeReadBytes": {"stat": "Sum", "unit": "Bytes"},
            "VolumeWriteBytes": {"stat": "Sum", "unit": "Bytes"}
        }
        for metric, params in metrics.items():
            data = _get_daily_metric_stats(
                cw_client,
                namespace="AWS/EBS",
                metric_name=metric,
                dimension_name="VolumeId",
                dimension_value=volume_id,
                days=days,
                stat=params["stat"],
                unit=params["unit"]
            )
            utilization[metric] = data
        vol_data["Utilization"] = utilization

    return vol_data


def _get_daily_metric_stats(
    cw_client,
    namespace,
    metric_name,
    dimension_name,
    dimension_value,
    days=14,
    stat="Average",
    unit=None
):
    """
    Generic helper to fetch daily statistics for a given metric over the last X days.
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
            Dimensions=[{"Name": dimension_name, "Value": dimension_value}],
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
