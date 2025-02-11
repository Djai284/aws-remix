# Optional common helper functions for collectors

def safe_get(d, *keys):
    """Safely get nested dictionary values."""
    for key in keys:
        d = d.get(key, {})
    return d

def get_boto3_client(service, region=None):
    """
    Return a boto3 client for the given service.
    """
    import boto3
    
    if region:
        return boto3.client(service, region_name=region)
    return boto3.client(service)
  
def pretty_print(data):
    """
    Pretty-print a data structure.
    """
    import json
    print(json.dumps(data, indent=2))

