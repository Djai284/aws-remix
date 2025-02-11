import boto3

def collect_vpc_info(region):
    ec2_client = boto3.client('ec2', region_name=region)
    vpcs = []
    try:
        response = ec2_client.describe_vpcs()
        for vpc in response.get("Vpcs", []):
            vpcs.append({
                "VpcId": vpc.get("VpcId"),
                "CidrBlock": vpc.get("CidrBlock"),
                "IsDefault": vpc.get("IsDefault")
            })
    except Exception as e:
        vpcs.append({"error": str(e)})
    return vpcs
