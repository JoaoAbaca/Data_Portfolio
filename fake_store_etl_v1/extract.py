import requests
import json
import os
import logging

# Configuración del logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Ruta de guardado
output_path = "data/raw/products.json"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# URL de la API
url = "https://fakestoreapi.com/products"

def validar_esquema(producto):
    """Verifica que el producto tenga las claves esperadas."""
    claves_esperadas = {'id', 'title', 'price', 'description', 'category', 'image', 'rating'}
    return claves_esperadas.issubset(producto.keys())

def extraer_datos():
    try:
        logging.info(f"Solicitando datos desde {url}...")
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if not isinstance(data, list):
            raise ValueError("La respuesta de la API no es una lista de productos.")

        # Validación básica de esquema
        datos_validos = [p for p in data if validar_esquema(p)]
        if len(datos_validos) < len(data):
            logging.warning("⚠️ Algunos productos fueron descartados por esquema incompleto.")

        # Guardar archivo
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(datos_validos, f, indent=2, ensure_ascii=False)

        logging.info(f"✅ Datos extraídos y guardados correctamente en {output_path}")
    except Exception as e:
        logging.error(f"❌ Error al extraer los datos: {e}")

if __name__ == "__main__":
    extraer_datos()
