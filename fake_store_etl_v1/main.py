# main.py

from extract import extraer_datos
from transform import main as transformar_datos
from load import main as cargar_datos
import logging

# Configurar logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

if __name__ == "__main__":
    logging.info("🚀 Iniciando pipeline ETL Fake Store")
    extraer_datos()
    transformar_datos()
    cargar_datos()
    logging.info("✅ Pipeline completado correctamente.")
