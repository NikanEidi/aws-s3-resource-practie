import boto3
from botocore.exceptions import ClientError

#* create resource
s3 = boto3.resource('s3', region_name='ca-central-1')

# declare bucket name
bucket_name = ""

def check_file_info(object_name="test.txt", Bucket=bucket_name):
    """
    Check file information from an S3 bucket using boto3 resource interface
    :param object_name: S3 object name (filename)
    :param Bucket: Name of the S3 bucket
    """
    try:
        obj = s3.Object(Bucket, object_name)
        obj.load()  # Fetches metadata from S3
        print(f"File: {object_name}")
        print(f"Size (bytes): {obj.content_length}")
        print(f"Content Type: {obj.content_type}")
        print(f"Metadata: {obj.metadata}")
    except ClientError as e:
        if e.response['Error']['Code'] == "404":
            print(f"File '{object_name}' does not exist in bucket '{Bucket}'.")
        else:
            print(f"Error occurred: {e}")

check_file_info()
