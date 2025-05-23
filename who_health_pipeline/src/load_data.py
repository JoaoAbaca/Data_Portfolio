import os
import pandas as pd
from sqlalchemy import create_engine, Table, Column, MetaData, String, Integer, Float

# Variables de entorno (revisar si están definidas en tu .env o docker-compose)
DB_USER = os.getenv("POSTGRES_USER", "airflow")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "airflow")
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "airflow")
TABLE_NAME = "who_health_data"

TRANSFORMED_DATA_PATH = os.path.join("data", "transformed_data.csv")

def load_data(file_path=TRANSFORMED_DATA_PATH):
    try:
        df = pd.read_csv(file_path)

        engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
        metadata = MetaData()

        table = Table(TABLE_NAME, metadata,
            Column("IndicatorCode", String),
            Column("SpatialDim", String),
            Column("ParentLocation", String),
            Column("TimeDim", Integer),
            Column("NumericValue", Float),
            Column("Low", Float),
            Column("High", Float),
            Column("Dim1", String),
        )

        # Crear tabla si no existe
        metadata.create_all(engine)

        # Cargar datos
        df.to_sql(TABLE_NAME, engine, if_exists="replace", index=False)
        print(f"Datos cargados correctamente en la tabla '{TABLE_NAME}'.")

    except Exception as e:
        print("Error al cargar datos:", e)

if __name__ == "__main__":
    load_data()
