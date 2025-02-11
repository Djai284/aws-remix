import boto3
import datetime

def _collect_30day_unblended_cost():
    ce_client = boto3.client('ce')
    end_date_obj = datetime.datetime.utcnow().date()
    start_date_str = (end_date_obj - datetime.timedelta(days=30)).isoformat()
    end_date_str = end_date_obj.isoformat()

    summary = {
        "TimePeriod": {"Start": start_date_str, "End": end_date_str},
        "TotalUnblendedCost": 0.0
    }

    try:
        response = ce_client.get_cost_and_usage(
            TimePeriod={'Start': start_date_str, 'End': end_date_str},
            Granularity='MONTHLY',
            Metrics=['UnblendedCost']
        )
        cost_data = response.get("ResultsByTime", [])
        if cost_data:
            amount_str = cost_data[0].get("Total", {}).get("UnblendedCost", {}).get("Amount", "0.0")
            summary["TotalUnblendedCost"] = float(amount_str)
        else:
            summary["message"] = "No cost data found."
    except Exception as e:
        summary["error"] = str(e)
    return summary

def collect_cost_for_all_regions(last_n_days=90):
    ce_client = boto3.client('ce')
    end_date_obj = datetime.datetime.utcnow().date()
    start_date_obj = end_date_obj - datetime.timedelta(days=last_n_days)
    start_date_str = start_date_obj.isoformat()
    end_date_str = end_date_obj.isoformat()

    region_cost_data = {
        "StartDate": start_date_str,
        "EndDate": end_date_str,
        "RegionCosts": [],
        "TotalCost": 0.0
    }

    try:
        resp = ce_client.get_cost_and_usage(
            TimePeriod={'Start': start_date_str, 'End': end_date_str},
            Granularity='MONTHLY',
            Metrics=['UnblendedCost'],
            GroupBy=[{"Type": "DIMENSION", "Key": "REGION"}]
        )
        results = resp.get("ResultsByTime", [])
        total_cost = 0.0
        region_accumulator = {}
        for monthly_data in results:
            for group in monthly_data.get("Groups", []):
                region_name = group["Keys"][0]  # e.g. "US East (N. Virginia)"
                amount = float(group["Metrics"]["UnblendedCost"]["Amount"])
                region_accumulator[region_name] = region_accumulator.get(region_name, 0.0) + amount
                total_cost += amount
        region_cost_list = []
        for region, cost_val in region_accumulator.items():
            region_cost_list.append({"Region": region, "Cost": cost_val})
        region_cost_data["RegionCosts"] = sorted(
            region_cost_list, key=lambda x: x["Cost"], reverse=True
        )
        region_cost_data["TotalCost"] = total_cost
    except Exception as e:
        region_cost_data["error"] = str(e)
    return region_cost_data

def find_relevant_regions_by_cost(region_cost_data, threshold_fraction=0.05, top_n=5):
    """
    Returns region codes that contribute at least threshold_fraction of the total cost.
    For example, if threshold_fraction is 0.05 then only regions that contribute 5% or more are returned.
    The region display names (e.g. "US East (N. Virginia)") are mapped to region codes.
    """

    if "RegionCosts" not in region_cost_data:
        return []
    total_cost = region_cost_data.get("TotalCost", 0.0)
    if total_cost == 0:
        return []
    # Select regions whose cost is at least threshold_fraction of the total
    filtered = [r for r in region_cost_data["RegionCosts"] if (r["Cost"] / total_cost) >= threshold_fraction]
    filtered = sorted(filtered, key=lambda x: x["Cost"], reverse=True)
    if len(filtered) > top_n:
        filtered = filtered[:top_n]
    relevant = []
    for item in filtered:
        region_code = item["Region"]
        if region_code:
            relevant.append(region_code)
    return relevant

def collect_3mo_cost_breakdown_and_forecast(last_n_days=90):
    ce_client = boto3.client('ce')
    end_date_obj = datetime.datetime.utcnow().date()
    start_date_obj = end_date_obj - datetime.timedelta(days=last_n_days)
    start_date_str = start_date_obj.isoformat()
    end_date_str = end_date_obj.isoformat()

    report = {
        "TimePeriod": {"Start": start_date_str, "End": end_date_str},
        "CostByService": [],
        "CostByRegion": [],
        "Forecast": {},
        "TotalCost": 0.0
    }

    try:
        svc_resp = ce_client.get_cost_and_usage(
            TimePeriod={'Start': start_date_str, 'End': end_date_str},
            Granularity='MONTHLY',
            Metrics=['UnblendedCost'],
            GroupBy=[{"Type": "DIMENSION", "Key": "SERVICE"}]
        )
        service_map = {}
        for period in svc_resp.get("ResultsByTime", []):
            for grp in period.get("Groups", []):
                svc_name = grp["Keys"][0]
                amt = float(grp["Metrics"]["UnblendedCost"]["Amount"])
                service_map[svc_name] = service_map.get(svc_name, 0.0) + amt
        total_cost = 0.0
        for sname, sval in service_map.items():
            total_cost += sval
            report["CostByService"].append({"Service": sname, "Amount": sval})
        reg_resp = ce_client.get_cost_and_usage(
            TimePeriod={'Start': start_date_str, 'End': end_date_str},
            Granularity='MONTHLY',
            Metrics=['UnblendedCost'],
            GroupBy=[{"Type": "DIMENSION", "Key": "REGION"}]
        )
        region_map = {}
        for period in reg_resp.get("ResultsByTime", []):
            for grp in period.get("Groups", []):
                rname = grp["Keys"][0]
                amt = float(grp["Metrics"]["UnblendedCost"]["Amount"])
                region_map[rname] = region_map.get(rname, 0.0) + amt
        for rname, rval in region_map.items():
            report["CostByRegion"].append({"Region": rname, "Amount": rval})
        report["TotalCost"] = total_cost

        forecast_resp = ce_client.get_cost_forecast(
            TimePeriod={
                'Start': end_date_str,
                'End': (end_date_obj + datetime.timedelta(days=30)).isoformat()
            },
            Metric='UNBLENDED_COST',
            Granularity='MONTHLY'
        )
        if "ForecastResultsByTime" in forecast_resp:
            forecast_item = forecast_resp["ForecastResultsByTime"][0]
            mean_val = forecast_item.get("MeanValue", "0.0")
            report["Forecast"]["TotalCostForecast"] = float(mean_val)
        else:
            report["Forecast"]["TotalCostForecast"] = 0.0
    except Exception as e:
        report["error"] = str(e)
    return report

def collect_cost_info(days_for_breakdown=90, threshold_fraction=0.05, top_n=10):
    """
    Generate a comprehensive cost section that includes:
      1) A 30-day unblended cost summary.
      2) A 90-day cost breakdown by region.
      3) A list of relevant regions (those contributing at least threshold_fraction of the total cost).
      4) A 3-month breakdown by service and region plus a cost forecast.
    """
    thirty_day_cost = _collect_30day_unblended_cost()
    region_cost_data = collect_cost_for_all_regions(last_n_days=days_for_breakdown)
    relevant_regions = find_relevant_regions_by_cost(region_cost_data, threshold_fraction=threshold_fraction, top_n=top_n)
    three_month_report = collect_3mo_cost_breakdown_and_forecast(last_n_days=days_for_breakdown)
    return {
        "ThirtyDayCost": thirty_day_cost,
        "RegionCosts90Day": region_cost_data,
        "RelevantRegions": relevant_regions,    # e.g. ["us-east-1", "us-west-2"]
        "ThreeMonthCostBreakdown": three_month_report
    }
