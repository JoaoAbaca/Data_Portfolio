# extract.py

import requests
import os
import json
from datetime import datetime

# Crear carpeta para datos si no existe
os.makedirs("data", exist_ok=True)

# Definir parámetros para la API
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1,
    "sparkline": False
}

# Realizar solicitud
response = requests.get(url, params=params)

# Validar respuesta
if response.status_code == 200:
    data = response.json()

    # Guardar resultado en archivo
    timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = f"data/raw_coin_data.json"

    with open(output_file, "w") as f:
        json.dump(data, f, indent=2)

    print(f"✅ Datos extraídos y guardados en: {output_file}")
else:
    print(f"❌ Error en la solicitud: {response.status_code}")
