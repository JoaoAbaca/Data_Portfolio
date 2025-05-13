import pandas as pd
import os
import json
from datetime import datetime


def transform_crypto_data():
    # Buscar el último archivo JSON en data/raw
    raw_dir = os.path.join("data", "raw")
    files = sorted(
        [f for f in os.listdir(raw_dir) if f.endswith(".json")],
        reverse=True
    )

    if not files:
        raise FileNotFoundError("No se encontraron archivos .json en data/raw")

    latest_file = os.path.join(raw_dir, files[0])
    with open(latest_file, "r") as f:
        data = json.load(f)

    # Convertir a DataFrame
    df = pd.DataFrame(data)

    # Limpiar y seleccionar columnas clave
    df_clean = df[["id", "symbol", "name", "current_price", "market_cap", "total_volume", "last_updated"]].copy()

    # Asegurar que el directorio 'data/processed' exista
    processed_dir = os.path.join("data", "processed")
    os.makedirs(processed_dir, exist_ok=True)

    # Guardar como CSV con timestamp
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(processed_dir, f"crypto_data_clean_{timestamp}.csv")
    df_clean.to_csv(output_file, index=False)

    print(f"✅ Datos transformados y guardados en {output_file}")
    return output_file

# Ejecutar directamente si se corre este script
if __name__ == "__main__":
    transform_crypto_data()
