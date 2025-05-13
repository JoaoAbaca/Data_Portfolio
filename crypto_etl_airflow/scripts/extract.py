import requests
import json
import os
from datetime import datetime


def extract_crypto_data():
    # Asegurar que el directorio 'data/raw' exista
    raw_dir = os.path.join("data", "raw")
    os.makedirs(raw_dir, exist_ok=True)

    # URL de la API
    url = "https://api.coingecko.com/api/v3/coins/markets"
    
    # Parámetros para obtener los 10 principales criptoactivos
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1,
        "sparkline": False
    }

    # Hacer la solicitud
    response = requests.get(url, params=params)
    data = response.json()

    # Crear nombre de archivo con timestamp
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(raw_dir, f"crypto_data_{timestamp}.json")

    # Guardar como JSON
    with open(output_path, "w") as f:
        json.dump(data, f, indent=4)

    print(f"✅ Datos extraídos y guardados en {output_path}")
    return output_path  # <- importante para usar en ETL

# Ejecutar directamente si se corre este script
if __name__ == "__main__":
    extract_crypto_data()
