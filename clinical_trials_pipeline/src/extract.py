import pandas as pd
import os
import logging

# Configurar logging
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "extract.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(log_file, mode='a'),
        logging.StreamHandler()
    ]
)

# Ruta al CSV original descargado manualmente
csv_source = "C:/Users/User/Desktop/Data_Portfolio/clinical_trials_pipeline/data/clinical_trials_diabetes.csv"
csv_clean = "C:/Users/User/Desktop/Data_Portfolio/clinical_trials_pipeline/data/studies_clean.csv"

# Verificar que el archivo original exista
if not os.path.exists(csv_source):
    logging.error(f"Archivo de entrada no encontrado: {csv_source}")
    raise FileNotFoundError(f"❌ No se encuentra el archivo CSV: {csv_source}")

# Leer y guardar copia limpia
try:
    df = pd.read_csv(csv_source)
    df.to_csv(csv_clean, index=False)
    logging.info(f"Archivo leído y guardado correctamente como: {csv_clean}")
    logging.info(f"Total de registros: {len(df)}")
except Exception as e:
    logging.error(f"Error al procesar archivo CSV: {e}")
    raise
