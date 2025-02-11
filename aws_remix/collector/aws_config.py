import boto3
import datetime

def collect_config_info(region=None):
    """
    Collects AWS Config rules and compliance statuses in the specified region.
    If no region is provided, uses the default Config client (often us-east-1).
    """
    if region:
        client = boto3.client('config', region_name=region)
    else:
        client = boto3.client('config')

    config_summary = {"Rules": [], "ComplianceByConfigRule": []}
    try:
        # List Config Rules
        paginator = client.get_paginator('describe_config_rules')
        for page in paginator.paginate():
            for rule in page.get('ConfigRules', []):
                config_summary["Rules"].append({
                    "ConfigRuleName": rule.get("ConfigRuleName"),
                    "Description": rule.get("Description"),
                    "Scope": rule.get("Scope", {}),
                    "Source": rule.get("Source", {}),
                    "CreatedBy": rule.get("CreatedBy")
                })

        # Get Compliance for each rule
        paginator = client.get_paginator('describe_compliance_by_config_rule')
        for page in paginator.paginate():
            for compliance in page.get('ComplianceByConfigRules', []):
                config_summary["ComplianceByConfigRule"].append({
                    "ConfigRuleName": compliance.get("ConfigRuleName"),
                    "Compliance": compliance.get("Compliance", {})
                })
    except Exception as e:
        config_summary["error"] = str(e)

    return config_summary
