# dags/who_health_pipeline.py

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os

# === Script paths ===
# Absolute path to each of the Python scripts in the pipeline
EXTRACT_SCRIPT = os.path.join(os.getcwd(), "src", "extract_data.py")
VALIDATE_SCRIPT = os.path.join(os.getcwd(), "src", "validate_data.py")
TRANSFORM_SCRIPT = os.path.join(os.getcwd(), "src", "transform_data.py")
LOAD_SCRIPT = os.path.join(os.getcwd(), "src", "load_data.py")

#=== Function to execute external scripts ===
def run_script(script_path):
    """
    Ejecuta un script Python desde su ruta absoluta.
    """
    os.system(f"python {script_path}")

# === Default DAG Configuration ===
default_args = {
    "start_date": datetime(2024, 1, 1),
    "retries": 1, # Retry once if a task fails
}

# === DAG Definition ===
with DAG(
    dag_id="who_health_pipeline",
    default_args=default_args,
    schedule_interval="@weekly",  # Run once a week
    catchup=False,                # Do not attempt to execute past executions
    tags=["who", "health"],
    description="ETL pipeline for WHO Health data using Python scripts",
) as dag:

# === Pipeline Tasks ===

    # 1. Extracting data from the WHO API
    extract = PythonOperator(
        task_id="extract_data",
        python_callable=run_script,
        op_args=[EXTRACT_SCRIPT],
    )

    # 2. Validation of the extracted data
    validate = PythonOperator(
        task_id="validate_data",
        python_callable=run_script,
        op_args=[VALIDATE_SCRIPT],
    )

    # 3. Data transformation and cleaning
    transform = PythonOperator(
        task_id="transform_data",
        python_callable=run_script,
        op_args=[TRANSFORM_SCRIPT],
    )

    # 4. Loading the processed data into PostgreSQL
    load = PythonOperator(
        task_id="load_data",
        python_callable=run_script,
        op_args=[LOAD_SCRIPT],
    )

    # === Dependencies between tasks ===
    extract >> validate >> transform >> load
