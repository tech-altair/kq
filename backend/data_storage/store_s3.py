import boto3
import json
import os

s3 = boto3.client('s3')

def store_in_data_lake(bucket_name, file_name, data):
    s3.put_object(Bucket=bucket_name, Key=file_name, Body=json.dumps(data))

store_in_data_lake('my-data-lake', 'raw_data.json', {'sample_data': 'value'})
