# src/load_data.py

import os
import pandas as pd
from sqlalchemy import create_engine

# Environment variables (defined in Docker/Airflow environment)
DB_USER = os.getenv("POSTGRES_USER", "airflow")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "airflow")
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "airflow")

# Path to processed CSV files
PROCESSED_DIR = os.path.join("data", "processed")

def load_all_transformed_data():
    """
    Load all processed CSV files into PostgreSQL.
    Table name = file name without extension.
    """
    try:
        engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

        for file in os.listdir(PROCESSED_DIR):
            if file.endswith(".csv"):
                file_path = os.path.join(PROCESSED_DIR, file)
                df = pd.read_csv(file_path)

                table_name = os.path.splitext(file)[0].lower()
                df.to_sql(table_name, engine, if_exists="replace", index=False)
                print(f"✅ Data loaded into table: '{table_name}' ({len(df)} records)")

    except Exception as e:
        print("❌ Error loading data:", e)

if __name__ == "__main__":
    load_all_transformed_data()
