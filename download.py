import boto3

s3 = boto3.resource('s3', region_name='ca-central-1')

bucket_name = "nikan-s3-resource-demo"

def download(Bucket=bucket_name, object_name="test.txt", file_name="downloaded_test.txt"):
    """
    Download a file from an S3 bucket using boto3 resource interface
    """
    s3.Bucket(Bucket).download_file(Key=object_name, Filename=file_name)

download()