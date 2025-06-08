import boto3
from botocore.exceptions import ClientError

s3 = boto3.resource('s3', region_name='ca-central-1')

bucket_name = "nikan-s3-resource-demo"

def delete_file(object_name=None, Bucket=bucket_name):
    """
    Delete a file from an S3 bucket using boto3 resource interface
    """
    try:
        s3.Object(Bucket, object_name).delete()
        print(f"'{object_name}' deleted from '{Bucket}'.")
    except ClientError as e:
        print(f"Error deleting '{object_name}' from '{Bucket}': {e}")

delete_file("test.txt")