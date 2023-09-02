import boto3

# Specify your AWS credentials and S3 bucket information
aws_access_key_id = 'AKIASKXEWL23FQYYHMEZ'
aws_secret_access_key = 'H0Gc8Y5Vn5cW5dOzvZ4YF1ckoTcT/wjSMF5k5IeY'
bucket_name = 'bot-practice-bucket'

# Initialize an S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# Specify the local file path and desired S3 key (path) within the bucket
local_file_path = 'C:\AWS Test Folder\CountryCoffeeData.csv'
s3_key = 'data/countryCoffeeData.csv'  # Adjust this as needed

# Upload the file to S3
s3.upload_file(local_file_path, bucket_name, s3_key)

print(f'File "{local_file_path}" uploaded to S3 bucket "{bucket_name}" as "{s3_key}"')
