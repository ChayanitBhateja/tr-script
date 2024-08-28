import os
import boto3
from botocore.exceptions import NoCredentialsError

def upload_to_s3(file_name, object_name=None):
    """
    Upload a file to an S3 bucket

    :param file_name: File to upload
    :param object_name: S3 object name. If not specified, file_name is used
    :return: True if file was uploaded, else False
    """
    # Get the bucket name from environment variable
    # BUCKET = os.getenv("S3_BUCKET_NAME")
    BUCKET = 'tr-bckt'

    # Check if bucket name is not None
    if BUCKET is None:
        print("S3 bucket name is not set as an environment variable")
        return False

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client("s3")
    try:
        s3_client.upload_file(file_name, BUCKET, object_name)
        print(f"File '{file_name}' uploaded to '{BUCKET}/{object_name}'")
        return True
    except FileNotFoundError:
        print(f"The file '{file_name}' was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


# Example usage
if __name__ == "__main__":
    file_name = "./ChayanitBhatejaDataScientistResume.pdf"
    upload_to_s3(file_name)
