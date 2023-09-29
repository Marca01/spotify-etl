import dags.tasks.Extract as Extract
import dags.tasks.Transform as Transform
# import sqlalchemy
# from sqlalchemy.orm import sessionmaker
import os
from google.cloud import storage

os.environ[
    "GOOGLE_APPLICATION_CREDENTIALS"
] = "/usr/local/airflow/dags/ServiceKey_GoogleCloudStorage.json"


def upload_to_gcs(contents, destination_blob_name):
    storage_client = storage.Client()
    bucket_name = os.getenv("BUCKET_NAME")
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_string(contents, content_type="application/json")
    print(f"{destination_blob_name} uploaded to {bucket_name}.")

def upload(transformed_data):
    load_df = Extract.return_dataframe()
    if Transform.data_quality(load_df) == False:
        raise "Failed at Data Validation"

    file_path = f'recently-played/favorite-artists.json'

    contents = transformed_data.to_json()

    upload_to_gcs(contents, file_path)

