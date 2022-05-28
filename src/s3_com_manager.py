# Manages S3 communication

import boto3, logging   # AWS libraries
import os

def upload_file_to_s3(origin_file_name: str, file_name: str) -> bool:
    """Uploads a file into S3 bucket folder"""
    s3_client = boto3.client(
        's3'
    )
    try:
        s3_client.upload_file(
            origin_file_name,
            os.environ.get('BUCKETNAME'),
            os.environ.get('BUCKETFOLDER')+"/"+file_name
        )
    except Exception as err:
        logging.error(err)
        return False
    return True