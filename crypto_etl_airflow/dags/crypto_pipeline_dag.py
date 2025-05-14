from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

# Add path so scripts can be imported from /scripts
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))

from extract import extract_crypto_data
from transform import transform_crypto_data
from load import load_to_postgres

default_args = {
    'owner': 'Joao',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='crypto_etl_pipeline',
    default_args=default_args,
    description='Un DAG simple de ETL para criptomonedas',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False
) as dag:

    task_extract = PythonOperator(
        task_id='extract_data',
        python_callable=extract_crypto_data
    )

    task_transform = PythonOperator(
        task_id='transform_data',
        python_callable=transform_crypto_data
    )

    task_load = PythonOperator(
    task_id='load_data',
    python_callable=load_to_postgres
    )

    task_extract >> task_transform >> task_load
