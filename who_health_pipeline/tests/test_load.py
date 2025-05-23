# tests/test_load.py

import os
import pandas as pd
import pytest
import psycopg2
from sqlalchemy import create_engine
from src.extract_data import extract_data
from src.validate_data import validate_data
from src.transform_data import transform_data
from src.load_data import load_data, TABLE_NAME

DB_USER = os.getenv("POSTGRES_USER", "airflow")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "airflow")
DB_HOST = os.getenv("POSTGRES_HOST", "postgres")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "airflow")

def test_load_data():
    # Ejecutar pipeline completo hasta la carga
    extract_data()
    validate_data()
    transform_data()
    load_data()

    # Verificar conexión y existencia de tabla
    engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    with engine.connect() as conn:
        result = conn.execute(f"SELECT COUNT(*) FROM {TABLE_NAME}")
        count = result.scalar()

        assert count > 0, "La tabla fue creada pero está vacía."

        # Comprobar columnas esperadas
        df = pd.read_sql_table(TABLE_NAME, conn)
        expected_cols = {"Country", "Location", "Period", "Sex", "Value", "IndicatorCode"}
        assert expected_cols.issubset(df.columns), f"Columnas faltantes: {expected_cols - set(df.columns)}"
