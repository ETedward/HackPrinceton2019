'''
Created on Nov 9, 2019

@author: mich2
'''
# Imports the Google Cloud client library
from google.cloud import storage

class CloudHandler():
    def __init__(self):
        self.storage_client = storage.Client.from_service_account_json(
        r"keyfile2.json")
        pass

    def upload_blob(self,bucket_name, source_file_name, destination_blob_name):
        # Uploads a file to the bucket.
        bucket = self.storage_client.get_bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
    
        blob.upload_from_filename(source_file_name)
    
        print('File {} uploaded to {}.'.format(
            source_file_name,
            destination_blob_name))
    def list_blobs(bucket_name):
        #"""Lists all the blobs in the bucket."""
        # storage_client = storage.Client()
    
        # Note: Client.list_blobs requires at least package version 1.17.0.
        blobs = self.storage_client.list_blobs(bucket_name)
    
        for blob in blobs:
            print(blob.name)