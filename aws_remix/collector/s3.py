import boto3

def collect_s3_info():
    s3_client = boto3.client('s3')
    buckets_info = []
    try:
        response = s3_client.list_buckets()
        for bucket in response.get("Buckets", []):
            bucket_name = bucket.get("Name")
            bucket_data = {
                "Name": bucket_name,
                "CreationDate": str(bucket.get("CreationDate")),
                # Tag this with relevant pillars:
                # - Security if we check encryption/public access
                # - Reliability if we check versioning
                # - Cost if we check lifecycle rules for cost-savings
                "Pillars": ["Security", "Reliability", "CostOptimization"]
            }

            # Optional: gather more security details
            try:
                enc = s3_client.get_bucket_encryption(Bucket=bucket_name)
                bucket_data["Encryption"] = enc.get("ServerSideEncryptionConfiguration", {})
            except s3_client.exceptions.ClientError:
                bucket_data["Encryption"] = "No explicit encryption or error retrieving."

            # Check public access
            try:
                public_block = s3_client.get_public_access_block(Bucket=bucket_name)
                bucket_data["PublicAccessBlock"] = public_block.get("PublicAccessBlockConfiguration")
            except s3_client.exceptions.ClientError:
                bucket_data["PublicAccessBlock"] = "Could not retrieve - possibly not set or no permission."

            buckets_info.append(bucket_data)

    except Exception as e:
        buckets_info.append({"error": str(e)})
    return buckets_info
