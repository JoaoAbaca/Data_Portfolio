# tests/test_validate.py

import os
import json
import pandas as pd
import pytest
from src.validate_data import validate_data, VALIDATED_DATA_PATH, schema
from src.extract_data import extract_data

def test_validate_data(tmp_path):
    # Extraemos datos reales primero (para tener un archivo válido)
    raw_path = tmp_path / "temp_raw.json"
    validated_path = tmp_path / "temp_validated.csv"

    # Usamos extract_data para generar datos reales
    extract_data(output_path=str(raw_path))

    # Ejecutamos validación
    validate_data(raw_path=str(raw_path), output_path=str(validated_path))

    # Verificamos que el archivo validado exista
    assert validated_path.exists(), "El archivo validado no fue creado."

    # Verificamos que se pueda leer con pandas
    df
