# tests/test_extract.py

import os
import json
import pytest
from src.extract_data import extract_data, OUTPUT_PATH

def test_extract_data_creates_file(tmp_path):
    # Ruta temporal para pruebas
    temp_output = tmp_path / "temp_raw.json"

    # Ejecutamos la función
    extract_data(output_path=str(temp_output))

    # Verificamos que el archivo se haya creado
    assert temp_output.exists(), "El archivo no fue creado por extract_data."

    # Verificamos que sea JSON válido
    with open(temp_output, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert isinstance(data, dict), "La respuesta no es un objeto JSON válido."
    assert "value" in data, "La clave 'value' no está en los datos de respuesta."

