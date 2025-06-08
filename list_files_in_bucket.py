import boto3
from botocore.exceptions import ClientError

#* create resource
s3 = boto3.resource('s3', region_name='ca-central-1')

# declare bucket name
bucket_name = ""

def list_files(Bucket=bucket_name):
    """
    List all files (objects) in a specified S3 bucket using boto3 resource interface
    :param Bucket: Name of the S3 bucket
    """
    try:
        bucket = s3.Bucket(Bucket)
        print(f"Files in bucket '{Bucket}':")
        for obj in bucket.objects.all():
            print(f"- {obj.key} ({obj.size} bytes)")
    except ClientError as e:
        print(f"Error listing files: {e}")

list_files()
