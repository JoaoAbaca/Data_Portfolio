import requests
import json
import os
import logging

# Logger configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Save path
output_path = "data/raw/products.json"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# API URL
url = "https://fakestoreapi.com/products"

def validar_esquema(producto):
    "Verify that the product has the expected keys."
    claves_esperadas = {'id', 'title', 'price', 'description', 'category', 'image', 'rating'}
    return claves_esperadas.issubset(producto.keys())

def extraer_datos():
    try:
        logging.info(f"Requesting data from {url}...")
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if not isinstance(data, list):
            raise ValueError("The API response is not a list of products.")

        # Basic schema validation
        datos_validos = [p for p in data if validar_esquema(p)]
        if len(datos_validos) < len(data):
            logging.warning("⚠️ Some products were discarded due to incomplete scheme.")

        # Save file
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(datos_validos, f, indent=2, ensure_ascii=False)

        logging.info(f"✅ Data extracted and saved correctly in {output_path}")
    except Exception as e:
        logging.error(f"❌ Error extracting data: {e}")

if __name__ == "__main__":
    extraer_datos()
