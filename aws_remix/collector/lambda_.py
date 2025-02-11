import boto3
import datetime

def collect_lambda_info(region, days=14):
    """
    Enhanced Lambda collector that:
      1) Lists Lambda functions with basic configuration details.
      2) Gathers CloudWatch metrics for key utilization metrics over the last `days`:
           - Invocations (Sum)
           - Duration (Average, in milliseconds)
           - Errors (Sum)
           - Throttles (Sum)
    Returns a list of Lambda function dictionaries including utilization data.
    """
    lambda_client = boto3.client('lambda', region_name=region)
    cw_client = boto3.client('cloudwatch', region_name=region)
    functions = []
    try:
        paginator = lambda_client.get_paginator('list_functions')
        for page in paginator.paginate():
            for function in page.get("Functions", []):
                function_name = function.get("FunctionName")
                func_data = {
                    "FunctionName": function_name,
                    "Runtime": function.get("Runtime"),
                    "LastModified": function.get("LastModified"),
                    "Handler": function.get("Handler"),
                    "MemorySize": function.get("MemorySize"),
                    "Timeout": function.get("Timeout"),
                    "Utilization": {}
                }
                # Collect CloudWatch metrics for the Lambda function.
                # For Lambda, we typically use "Sum" for count metrics and "Average" for duration.
                invocations = _get_daily_metric_stats(
                    cw_client,
                    namespace="AWS/Lambda",
                    metric_name="Invocations",
                    dimension_name="FunctionName",
                    dimension_value=function_name,
                    days=days,
                    stat="Sum",
                    unit="Count"
                )
                duration = _get_daily_metric_stats(
                    cw_client,
                    namespace="AWS/Lambda",
                    metric_name="Duration",
                    dimension_name="FunctionName",
                    dimension_value=function_name,
                    days=days,
                    stat="Average",
                    unit="Milliseconds"
                )
                errors = _get_daily_metric_stats(
                    cw_client,
                    namespace="AWS/Lambda",
                    metric_name="Errors",
                    dimension_name="FunctionName",
                    dimension_value=function_name,
                    days=days,
                    stat="Sum",
                    unit="Count"
                )
                throttles = _get_daily_metric_stats(
                    cw_client,
                    namespace="AWS/Lambda",
                    metric_name="Throttles",
                    dimension_name="FunctionName",
                    dimension_value=function_name,
                    days=days,
                    stat="Sum",
                    unit="Count"
                )
                func_data["Utilization"]["Invocations"] = invocations
                func_data["Utilization"]["Duration"] = duration
                func_data["Utilization"]["Errors"] = errors
                func_data["Utilization"]["Throttles"] = throttles

                functions.append(func_data)
    except Exception as e:
        functions.append({"error": str(e)})

    return functions


def _get_daily_metric_stats(
    cw_client,
    namespace,
    metric_name,
    dimension_name,
    dimension_value,
    days=14,
    stat="Sum",
    unit=None
):
    """
    Generic helper to fetch daily statistics for a given metric (used by Lambda collector).
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
