import boto3
import os
import pathlib
from botocore.exceptions import ClientError

s3 = boto3.resource('s3', region_name='ca-central-1')

bucket_name = ""

def upload_to_folder(folder_name="documents", file_name="test.txt", Bucket=bucket_name):
    """
    Upload a file to a virtual folder (prefix) in an S3 bucket using resource interface
    """
    try:
        file_path = os.path.join(pathlib.Path(__file__).parent.resolve(), file_name)
        
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write("This is a test file uploaded to a folder in S3 using resource.")

        object_key = f"{folder_name}/{file_name}"  # 'documents/test.txt'

        s3.Bucket(Bucket).upload_file(Filename=file_path, Key=object_key)
        print(f"'{file_name}' uploaded to folder '{folder_name}' in bucket '{Bucket}'.")
        
    except ClientError as e:
        print(f"Upload failed: {e}")

upload_to_folder()
