import datetime
import concurrent.futures
import boto3

from aws_remix.collector import (
    ec2, lambda_, s3, rds, ecs, vpc, iam, cost,
    aws_config, trusted_advisor, security_hub
)
from aws_remix.output import format_json, format_yaml, format_markdown
from aws_remix.scorecard import generate_scorecard

def get_aws_account_info():
    sts_client = boto3.client('sts')
    iam_client = boto3.client('iam')
    identity = sts_client.get_caller_identity()
    account = identity.get("Account", "N/A")
    try:
        aliases = iam_client.list_account_aliases().get("AccountAliases", [])
        account_alias = aliases[0] if aliases else "N/A"
    except Exception:
        account_alias = "N/A"
    return {"AccountNumber": account, "AccountAlias": account_alias}

def get_all_active_regions():
    ec2_client = boto3.client('ec2')
    regions_response = ec2_client.describe_regions(AllRegions=True)
    active_regions = [
        region["RegionName"]
        for region in regions_response.get("Regions", [])
        if region.get("OptInStatus", "opt-in-not-required") in ["opt-in-not-required", "opted-in"]
    ]
    return active_regions

def collect_all_regions(func, regions):
    """
    Helper that concurrently collects data for all regions.
    'func' is expected to be a function that accepts a region name.
    Returns a dict mapping region to its results.
    """
    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(regions)) as executor:
        future_to_region = {executor.submit(func, region): region for region in regions}
        for future in concurrent.futures.as_completed(future_to_region):
            region = future_to_region[future]
            try:
                results[region] = future.result()
            except Exception as e:
                results[region] = {"error": str(e)}
    return results
  
def generate_full_summary(regions=None, lens=None, progress=None):
    """
    Generate the full report as a dictionary.
    If regions is None, scans all active regions.
    The optional 'progress' parameter (a Rich Progress instance)
    is used to update the progress bar as each collector completes.
    """
    if regions is None:
        regions = get_all_active_regions()

    summary = {}
    summary["ReportGenerated"] = datetime.datetime.now().isoformat()
    summary["AccountInfo"] = get_aws_account_info()
    summary["ActiveRegions"] = regions

    # Create a dictionary of futures for independent collectors.
    futures = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        # Global / non-region collectors:
        if lens is None or lens == "cost":
            futures["Cost"] = executor.submit(cost.collect_cost_info)
        if lens is None or lens in ["security", "operational"]:
            futures["IAM"] = executor.submit(iam.collect_iam_info)
        if lens is None or lens in ["security", "operational"]:
            futures["TrustedAdvisor"] = executor.submit(trusted_advisor.collect_trusted_advisor_checks)
        if lens is None or lens == "security":
            futures["SecurityHub"] = executor.submit(security_hub.collect_security_hub_findings)
        if lens is None or lens in ["security", "operational"]:
            futures["S3"] = executor.submit(s3.collect_s3_info)
        
        # Region-based collectors:
        if lens is None or lens in ["security", "reliability", "performance", "cost", "sustainability"]:
            futures["EC2"] = executor.submit(collect_all_regions, ec2.collect_ec2_info_with_utilization, regions)
        if lens is None or lens in ["security", "performance", "operational", "cost"]:
            futures["Lambda"] = executor.submit(collect_all_regions, lambda_.collect_lambda_info, regions)
        if lens is None or lens in ["security", "performance", "operational", "cost"]:
            # Use enhanced ECS collector with utilization data
            futures["ECS"] = executor.submit(collect_all_regions, ecs.collect_ecs_info_with_utilization, regions)
        if lens is None or lens in ["security", "reliability", "performance", "cost"]:
            futures["RDS"] = executor.submit(collect_all_regions, rds.collect_rds_info, regions)
        if lens is None or lens in ["security", "reliability"]:
            futures["VPC"] = executor.submit(collect_all_regions, vpc.collect_vpc_info, regions)
        if lens is None or lens in ["security", "operational"]:
            futures["Config"] = executor.submit(collect_all_regions, aws_config.collect_config_info, regions)

        # If a progress object is passed in, create a progress task for each future.
        tasks = {}
        if progress is not None:
            tasks = { key: progress.add_task(f"Collecting {key}...", total=1) for key in futures.keys() }

        # Wait for each future to complete and update the progress.
        for key, future in futures.items():
            try:
                summary[key] = future.result()
                if progress is not None:
                    progress.update(tasks[key], completed=1, description=f"{key} completed")
            except Exception as e:
                summary[key] = {"error": str(e)}
                if progress is not None:
                    progress.update(tasks[key], completed=1, description=f"{key} failed")

    # Generate scorecard / findings based on the collected summary.
    scorecard = generate_scorecard(summary)
    summary["Findings"] = scorecard["Findings"]
    summary["Scores"] = scorecard["Scores"]

    return summary
  
def format_report(report, output_format):
    output_format = output_format.lower()
    if output_format == "json":
        return format_json(report)
    elif output_format in ["yaml", "yml"]:
        return format_yaml(report)
    elif output_format in ["txt", "readme", "markdown", "md"]:
        return format_markdown(report)
    else:
        return format_markdown(report)
