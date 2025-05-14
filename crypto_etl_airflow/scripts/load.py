import os
import pandas as pd
from sqlalchemy import create_engine, text
from glob import glob


def get_latest_csv_file(processed_dir="data/processed/"):
    csv_files = glob(os.path.join(processed_dir, "*.csv"))
    if not csv_files:
        raise FileNotFoundError("No se encontraron archivos CSV en data/processed/")
    latest_file = max(csv_files, key=os.path.getctime)
    return latest_file


def load_to_postgres():
    # Obtener el archivo CSV más reciente
    csv_file = get_latest_csv_file()
    df = pd.read_csv(csv_file)

    # Crear engine de conexión a PostgreSQL
    POSTGRES_USER = os.getenv("POSTGRES_USER", "airflow")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "airflow")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST", "postgres")
    POSTGRES_DB = os.getenv("POSTGRES_DB", "airflow")

    db_url = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"
    engine = create_engine(db_url)

    # Crear tabla si no existe
    table_name = "crypto_prices"
    with engine.connect() as conn:
        conn.execute(text(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id TEXT,
                symbol TEXT,
                name TEXT,
                current_price FLOAT,
                market_cap FLOAT,
                total_volume FLOAT,
                last_updated TEXT
            )
        """))

    # Cargar los datos al final de la tabla (append)
    df.to_sql(table_name, engine, if_exists='append', index=False)

    print(f"✅ Datos cargados en la tabla '{table_name}' de PostgreSQL")


if __name__ == "__main__":
    load_to_postgres()
