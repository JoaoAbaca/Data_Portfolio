import os
import json
import pandas as pd
from datetime import datetime
from glob import glob
import pandera as pa
from pandera import Column, DataFrameSchema


def get_latest_json_file(raw_dir="data/raw/"):
    json_files = glob(os.path.join(raw_dir, "*.json"))
    if not json_files:
        raise FileNotFoundError("No se encontraron archivos JSON en data/raw/")
    latest_file = max(json_files, key=os.path.getctime)
    return latest_file


# Definir el esquema de validación esperado
schema = DataFrameSchema({
    "id": Column(str),
    "symbol": Column(str),
    "name": Column(str),
    "current_price": Column(float),
    "market_cap": Column(float),
    "total_volume": Column(float),
    "last_updated": Column(str),
})


def transform_crypto_data():
    # Obtener archivo JSON más reciente
    input_file = get_latest_json_file()
    with open(input_file, "r") as f:
        data = json.load(f)

    # Cargar a DataFrame
    df = pd.DataFrame(data)

    # Seleccionar columnas relevantes
    df_clean = df[[
        "id", "symbol", "name",
        "current_price", "market_cap",
        "total_volume", "last_updated"
    ]].copy()

    # Convertir columnas numéricas a float para asegurar compatibilidad con el esquema
    num_cols = ["current_price", "market_cap", "total_volume"]
    df_clean[num_cols] = df_clean[num_cols].astype(float)

    # Validar datos
    schema.validate(df_clean)

    # Crear carpeta de salida si no existe
    output_dir = "data/processed"
    os.makedirs(output_dir, exist_ok=True)

    # Guardar CSV con timestamp
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(output_dir, f"crypto_data_clean_{timestamp}.csv")
    df_clean.to_csv(output_file, index=False)

    print(f"✅ Datos transformados y validados. Archivo guardado en {output_file}")
    return output_file


if __name__ == "__main__":
    transform_crypto_data()
