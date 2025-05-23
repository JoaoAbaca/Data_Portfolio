# dags/who_health_pipeline_dag.py

import sys
sys.path.append('/opt/airflow/src') 

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from extract_data import extract_data
from validate_data import validate_data
from transform_data import transform_data
from load_data import load_data

default_args = {
    "owner": "joao",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="who_health_pipeline",
    default_args=default_args,
    description="Pipeline de datos desde la API de la OMS hacia PostgreSQL",
    schedule_interval="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["OMS", "ETL", "salud"],
) as dag:

    extract_task = PythonOperator(
        task_id="extract_data",
        python_callable=extract_data,
    )

    validate_task = PythonOperator(
        task_id="validate_data",
        python_callable=validate_data,
    )

    transform_task = PythonOperator(
        task_id="transform_data",
        python_callable=transform_data,
    )

    load_task = PythonOperator(
        task_id="load_data",
        python_callable=load_data,
    )

    extract_task >> validate_task >> transform_task >> load_task
