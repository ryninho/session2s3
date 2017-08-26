"""
Save session to S3 bucket. Ex: ses2s3.workspace_to_s3('my-project-script')
"""
from datetime import datetime
import re

import boto3
import dill

def session_to_s3(prefix, bucket_name, timestamp=True):
  """Save session to S3 bucket. Login via ~/.aws/credentials as per boto3."""
  if timestamp:
    now_str = str(datetime.now())
    date_time_str = re.sub('[^0-9a-zA-Z]+', '_', now_str)
    filename = prefix + "_" + date_time_str + ".pkl"
  else:
    filename = prefix + ".pkl"
  dill.dump_session(filename)
  s3 = boto3.resource('s3')
  s3.meta.client.upload_file(filename, bucket_name, filename)
  return filename
