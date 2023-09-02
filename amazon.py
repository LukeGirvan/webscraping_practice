import boto3
import os 

# Specify your AWS credentials and S3 bucket information
aws_access_key_id = 'aws access key here'
aws_secret_access_key = 'secret acess key here'
bucket_name = 'bucket name here'

# Initialize an S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# Specify the local file path and desired S3 key (path) within the bucket
local_directory = 'C:\AWS Test Folder'
s3_directory = 'data/'  # Adjust this as needed
uploaded_files = set()

# List all objects in the S3 directory to check for duplicates
s3_objects = s3.list_objects(Bucket=bucket_name, Prefix=s3_directory)
if 'Contents' in s3_objects:
    for s3_object in s3_objects['Contents']:
        uploaded_files.add(os.path.basename(s3_object['Key']))

for filename in os.listdir(local_directory):
    filepath = os.path.join(local_directory, filename)
    if os.path.isfile(filepath):
        if filename not in uploaded_files:
            # Create the S3 key (path) for the file
            s3_key = os.path.join(s3_directory, filename).replace('\\', '/')
            
            # Upload the file to S3
            s3.upload_file(filepath, bucket_name, s3_key)
            
            print(f'File "{filename}" uploaded to S3 bucket "{bucket_name}" as "{s3_key}"')
        else:
            print(f'File "{filename}" already exists in S3 bucket and was skipped.')
