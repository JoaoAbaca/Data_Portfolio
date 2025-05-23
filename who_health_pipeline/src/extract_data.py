# src/extract_data.py

import requests
import os
import json
import pandas as pd

# Rutas y constantes
OUTPUT_PATH = os.path.join("data", "raw_data.json")
API_URL = "https://ghoapi.azureedge.net/api/WHOSIS_000001"

def extract_data(url: str = API_URL, output_path: str = OUTPUT_PATH):
    try:
        print(f"Solicitando datos desde {url}...")
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Guardar como archivo JSON
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Datos guardados en {output_path}")

        # --- INSPECCIÓN PRELIMINAR ---
        # Mostrar primeros registros y columnas si existen
        records = data.get("value", [])
        df_preview = pd.DataFrame(records)
        print("\nPreview de datos crudos:")
        print(df_preview.head())
        print("\nColumnas disponibles:")
        print(df_preview.columns.tolist())

    except requests.RequestException as e:
        print(f"Error al solicitar datos: {e}")
    except Exception as ex:
        print(f"Error inesperado: {ex}")

if __name__ == "__main__":
    extract_data()
