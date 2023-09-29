import datetime as dt
from airflow.operators.python_operator import PythonOperator
from airflow.decorators import (
    dag,
    task,
    task_group
)
from airflow.models.baseoperator import chain
from airflow.utils.dates import days_ago
from tasks.Extract import return_dataframe
from tasks.Transform import data_quality, transform_df
from tasks.Load import upload
from tasks.etl import spotify_etl

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(0),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=1)
}

@dag(
    default_args=default_args,
    schedule_interval='@daily',
    description='Spotify ETL process 1-min',
    catchup=False
    # schedule_interval=dt.timedelta(minutes=50)
)

def run_spotify_etl():
    @task
    def run_etl():
        spotify_etl()

    run_etl()

run_spotify_etl()




