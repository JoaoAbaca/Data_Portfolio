import pandas as pd
import os
from sqlalchemy import create_engine, text

def load_orders_to_postgres():
    # Ruta al archivo Excel
    excel_path = "data/orders.xlsx"
    df = pd.read_excel(excel_path)

    # Configuración de PostgreSQL (usando variables de entorno o defaults)
    POSTGRES_USER = os.getenv("POSTGRES_USER", "airflow")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "airflow")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST", "postgres")
    POSTGRES_DB = os.getenv("POSTGRES_DB", "airflow")

    db_url = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"
    engine = create_engine(db_url)

    # Crear tabla si no existe (sobreescribe si ya existe)
    table_name = "raw_orders"
    with engine.connect() as conn:
        conn.execute(text(f"DROP TABLE IF EXISTS {table_name}"))

    df.to_sql(table_name, engine, if_exists='replace', index=False)

    print(f"✅ Datos cargados en la tabla '{table_name}' en PostgreSQL")

if __name__ == "__main__":
    load_orders_to_postgres()
