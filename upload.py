import os
import boto3
from botocore.exceptions import NoCredentialsError, ClientError

def upload_files_to_s3(directory, bucket_name):
    """
    Upload all files in the specified directory to the given S3 bucket.

    :param directory: Directory containing files to upload
    :param bucket_name: S3 bucket name
    :return: None
    """
    # Initialize the S3 client
    s3_client = boto3.client('s3')

    # Check if directory exists
    if not os.path.isdir(directory):
        print(f"The directory '{directory}' does not exist.")
        return

    # Iterate over all files in the directory
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)

        # Skip directories, only upload files
        if os.path.isfile(file_path):
            try:
                # Upload the file
                s3_client.upload_file(file_path, bucket_name, file_name)
                print(f"File '{file_name}' uploaded to bucket '{bucket_name}'.")
            except FileNotFoundError:
                print(f"The file '{file_path}' was not found.")
            except NoCredentialsError:
                print("Credentials not available.")
            except ClientError as e:
                print(f"Failed to upload '{file_name}': {e}")

if __name__ == "__main__":
    # Example usage
    directory_to_upload = 'C:/path/to/your/directory'
    s3_bucket_name = 'your-bucket-name'
    
    upload_files_to_s3(directory_to_upload, s3_bucket_name)
