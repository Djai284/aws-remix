"""
scorecard.py

Provides a basic scanning mechanism that looks for common issues and
produces a "findings" list and optional numeric "score" per pillar.
This is just an example. You can refine the checks and scoring logic
to suit your needs.
"""
import json

def generate_scorecard(report):
    """
    Analyzes the full 'report' dictionary and returns a dictionary of
    findings categorized by pillar. Each finding has a severity, a message,
    and a reference to the resource(s).
    """
    findings = {
        "Security": [],
        "Reliability": [],
        "PerformanceEfficiency": [],
        "CostOptimization": [],
        "OperationalExcellence": [],
        "Sustainability": []
    }

    # 1. Example S3 check - no encryption
    if "S3" in report:
        for bucket in report["S3"]:
            # If we see 'No explicit encryption' text, raise a Security finding
            if isinstance(bucket, dict) and "Encryption" in bucket:
                if bucket["Encryption"] == "No explicit encryption or error retrieving.":
                    findings["Security"].append({
                        "Resource": bucket.get("Name"),
                        "Severity": "HIGH",
                        "Description": "S3 Bucket lacks explicit encryption settings."
                    })

    # 2. Example EC2 check - unencrypted EBS
    if "EC2" in report:
        region_data = report["EC2"].get("regions", {})
        for region, instances in region_data.items():
            for inst in instances:
                ebs_vols = inst.get("EBSVolumes", [])
                for vol in ebs_vols:
                    if vol.get("Encrypted") is False:
                        findings["Security"].append({
                            "Resource": inst.get("InstanceId"),
                            "Severity": "HIGH",
                            "Description": f"EBS Volume {vol['VolumeId']} is not encrypted.",
                            "Region": region
                        })

    # 3. Trusted Advisor cost-savings checks (example)
    if "TrustedAdvisor" in report:
        for check in report["TrustedAdvisor"]:
            category = check.get("Category")
            name = check.get("Name")
            result = check.get("Result", {})
            flagged_resources = result.get("flaggedResources", [])
            if category == "cost_optimizing" and flagged_resources:
                for resource in flagged_resources:
                    findings["CostOptimization"].append({
                        "CheckName": name,
                        "Severity": "MEDIUM",
                        "Resource": resource.get("resourceId"),
                        "Description": resource.get("status")
                    })

    # ... add more checks for Reliability, Performance, Ops Excellence, Sustainability, etc.

    # Optionally compute a simple "score" for each pillar
    pillar_scores = compute_pillar_scores(findings)

    return {
        "Findings": findings,
        "Scores": pillar_scores
    }


def compute_pillar_scores(findings):
    """
    Compute a naive 'score' for each pillar based on the number 
    and severity of findings. High severity might reduce the score 
    more than low severity, etc.
    """
    scores = {
        "Security": 100,
        "Reliability": 100,
        "PerformanceEfficiency": 100,
        "CostOptimization": 100,
        "OperationalExcellence": 100,
        "Sustainability": 100
    }

    # Example scoring logic
    severity_weights = {"HIGH": 20, "MEDIUM": 10, "LOW": 5}
    for pillar, items in findings.items():
        for item in items:
            sev = item.get("Severity", "MEDIUM").upper()
            penalty = severity_weights.get(sev, 10)
            scores[pillar] = max(0, scores[pillar] - penalty)

    return scores
