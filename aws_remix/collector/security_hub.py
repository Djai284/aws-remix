import boto3

def collect_security_hub_findings():
    """
    Collects Security Hub findings from all enabled standards (e.g. CIS, PCI).
    """
    securityhub = boto3.client('securityhub')
    findings_data = []

    try:
        paginator = securityhub.get_paginator('get_findings')
        for page in paginator.paginate():
            for finding in page.get('Findings', []):
                findings_data.append({
                    "Title": finding.get("Title"),
                    "Severity": finding.get("Severity"),
                    "Description": finding.get("Description"),
                    "Resources": finding.get("Resources"),
                    "CreatedAt": finding.get("CreatedAt"),
                    "UpdatedAt": finding.get("UpdatedAt"),
                    "SourceUrl": finding.get("SourceUrl")
                })
    except Exception as e:
        findings_data.append({"error": str(e)})

    return findings_data
