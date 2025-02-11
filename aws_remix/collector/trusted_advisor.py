import boto3

def collect_trusted_advisor_checks():
    """
    Collects summary data from AWS Trusted Advisor for cost optimization, 
    security, performance, fault tolerance, and service limits.
    Note: Must have Business or Enterprise support plan, 
    or this won't return full info.
    """
    support_client = boto3.client('support', region_name='us-east-1')  # Trusted Advisor is only in us-east-1
    checks_data = []

    try:
        # Retrieve all TA checks
        checks_response = support_client.describe_trusted_advisor_checks(language='en')
        checks = checks_response.get('checks', [])

        # For each check, get the result
        for check in checks:
            check_id = check.get('id')
            result = support_client.describe_trusted_advisor_check_result(
                checkId=check_id,
                language='en'
            )
            checks_data.append({
                "CheckId": check_id,
                "Name": check.get('name'),
                "Category": check.get('category'),
                "Description": check.get('description'),
                "Result": result.get('result')
            })
    except Exception as e:
        checks_data.append({"error": str(e)})

    return checks_data
