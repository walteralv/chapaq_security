import boto3
from core.config import Settings

def get_s3_client():
    return boto3.client('s3')
