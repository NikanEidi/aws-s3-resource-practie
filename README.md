# AWS S3 Resource Interface with Boto3

This project demonstrates how to use the **Boto3 resource interface** to interact with AWS S3 using Python. Unlike the low-level client API, the resource interface is more Pythonic and object-oriented, making S3 operations easier and cleaner to manage.

---

## 🚀 Features

- Create a bucket using resource interface  
- Upload files with optional custom names and paths  
- Download files from S3  
- Delete objects from a bucket  
- List all objects in a bucket  
- Upload to folder-like prefixes  
- Manage storage classes  
- Enable and use versioning  
- Generate secure pre-signed URLs  
- Transfer files between buckets  

---

## 🛠 Setup Instructions

1. **Install Boto3**  
   ```bash
   pip install boto3
   ```

2. **Configure AWS CLI**  
   ```bash
   aws configure
   ```
   Provide your Access Key ID, Secret Access Key, region (e.g. `ca-central-1`), and default output format (e.g. `json`).

> Ensure your IAM user has sufficient permissions (like `AmazonS3FullAccess`) for all the above operations.

---

## 📂 File Structure

Each file in this repo handles one key feature. For example:

- `upload_file.py` — Upload a file  
- `download_file.py` — Download a file  
- `delete_file.py` — Delete an object  
- `list_files.py` — List objects in a bucket  
- `upload_to_folder.py` — Upload into a folder (prefix)  
- ... and more

---

## 🔗 Related Projects

If you're looking for the **low-level client interface version**, check this out:  
👉 [AWS S3 Client Interface Repository](https://github.com/NikanEidi/aws-s3-client-practie)

---

## 📘 Author

This is part of **Nikan’s Summer Certificate Program – AWS Track** ☁️  
Repository created and maintained by [@NikanEidi](https://github.com/NikanEidi)
