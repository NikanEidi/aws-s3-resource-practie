import boto3
from botocore.exceptions import ClientError

s3 = boto3.resource('s3', region_name='ca-central-1')

bucket_name = "nikan-s3-resource-demo"

def list_files(Bucket=bucket_name):
    """
    List all files in a given S3 bucket using boto3 resource interface
    """
    try:
        bucket = s3.Bucket(Bucket)
        for obj in bucket.objects.all():
            print(obj.key)
    except ClientError as e:
        print(f"Error listing files in '{Bucket}': {e}")

list_files()