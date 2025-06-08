import boto3
import os
import pathlib  # provides methods for working with paths

# create the S3 resource
s3 = boto3.resource('s3', region_name='ca-central-1')

bucket_name = ""

def bucket():
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'ca-central-1'
        }
    )

def upload(file_name, bucket=bucket_name, object_name=None):
    """
    Upload a file using boto3.resource
    """
    file_path = os.path.join(pathlib.Path(__file__).parent.resolve(), "test.txt")
    
    if not os.path.exists(file_path):
        with open(file_path, "a") as f:
            f.write("This is resource Test by Me")
    
    if object_name is None:
        object_name = "test.txt"
    
    # Get the actual bucket object
    bucket_obj = s3.Bucket(bucket)
    bucket_obj.upload_file(Filename=file_path, Key=object_name)
    print("Upload successful")

upload("test.txt")
