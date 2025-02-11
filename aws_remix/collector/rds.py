import boto3

def collect_rds_info(region):
    rds_client = boto3.client('rds', region_name=region)
    db_instances = []
    try:
        response = rds_client.describe_db_instances()
        for db in response.get("DBInstances", []):
            db_instances.append({
                "DBInstanceIdentifier": db.get("DBInstanceIdentifier"),
                "Engine": db.get("Engine"),
                "DBInstanceStatus": db.get("DBInstanceStatus")
            })
    except Exception as e:
        db_instances.append({"error": str(e)})
    return db_instances
