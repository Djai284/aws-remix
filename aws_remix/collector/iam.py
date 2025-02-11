import boto3

def collect_iam_info():
    iam_client = boto3.client('iam')
    iam_summary = {}
    try:
        # Users
        users = []
        paginator = iam_client.get_paginator('list_users')
        for page in paginator.paginate():
            for user in page.get("Users", []):
                users.append({
                    "UserName": user.get("UserName"),
                    "CreateDate": str(user.get("CreateDate"))
                })
        iam_summary["Users"] = users
        
        # Roles
        roles = []
        paginator = iam_client.get_paginator('list_roles')
        for page in paginator.paginate():
            for role in page.get("Roles", []):
                roles.append({
                    "RoleName": role.get("RoleName"),
                    "CreateDate": str(role.get("CreateDate"))
                })
        iam_summary["Roles"] = roles
        
        # Policies
        policies = []
        paginator = iam_client.get_paginator('list_policies')
        for page in paginator.paginate(Scope='Local'):
            for policy in page.get("Policies", []):
                policies.append({
                    "PolicyName": policy.get("PolicyName"),
                    "CreateDate": str(policy.get("CreateDate"))
                })
        iam_summary["Policies"] = policies
    except Exception as e:
        iam_summary["error"] = str(e)
    return iam_summary
