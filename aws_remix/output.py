import json
import yaml

def format_json(report):
    return json.dumps(report, indent=4)

def format_yaml(report):
    return yaml.dump(report, default_flow_style=False)

def format_markdown(report):
    """
    Convert the report dictionary to a human-readable Markdown string.
    """
    lines = []
    lines.append("# AWS Remix Report")
    lines.append("")
    # Report metadata
    lines.append(f"**Report Generated:** {report.get('ReportGenerated', 'N/A')}")
    lines.append("")
    
    # Account Information
    account = report.get("AccountInfo", {})
    lines.append("## AWS Account Information")
    lines.append(f"- **Account Number:** {account.get('AccountNumber', 'N/A')}")
    lines.append(f"- **Account Alias:** {account.get('AccountAlias', 'N/A')}")
    active_regions = report.get("ActiveRegions", [])
    lines.append(f"- **Active Regions:** {', '.join(active_regions) if active_regions else 'N/A'}")
    lines.append("")

    # For each section (Cost, EC2, Lambda, ECS, S3, RDS, VPC, IAM), format nicely.
    for section in ["Cost", "EC2", "Lambda", "ECS", "S3", "RDS", "VPC", "IAM"]:
        if section not in report:
            continue
        lines.append(f"## {section}")
        lines.append("")
        lines.append(format_section(report[section]))
        lines.append("")
    return "\n".join(lines)

def format_section(section, indent=0):
    """
    Recursively format a section of the report.
    """
    indentation = "  " * indent
    if isinstance(section, dict):
        lines = []
        for key, value in section.items():
            lines.append(f"{indentation}- **{key}:**")
            lines.append(format_section(value, indent + 1))
        return "\n".join(lines)
    elif isinstance(section, list):
        if not section:
            return f"{indentation}- None"
        lines = []
        for item in section:
            lines.append(f"{indentation}- {format_section(item, indent + 1).strip()}")
        return "\n".join(lines)
    else:
        # For simple types, just return a string representation.
        return f"{indentation}{section}"
