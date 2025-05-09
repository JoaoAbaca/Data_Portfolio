import pandas as pd
import sqlite3
import os
import logging

# Configurar logging
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "load.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(log_file, mode='a'),
        logging.StreamHandler()
    ]
)

# Definir rutas
csv_path = "C:/Users/User/Desktop/Data_Portfolio/clinical_trials_pipeline/data/studies_transform.csv"
db_path = "C:/Users/User/Desktop/Data_Portfolio/clinical_trials_pipeline/database/clinical_trials.db"

# Verificar archivo CSV
if not os.path.exists(csv_path):
    logging.error(f"Archivo no encontrado: {csv_path}")
    raise FileNotFoundError(f"❌ El archivo CSV no se encontró: {csv_path}")

# Leer CSV
try:
    df = pd.read_csv(csv_path)
    logging.info(f"CSV leído correctamente. Registros: {len(df)}")
except Exception as e:
    logging.error(f"Error al leer el CSV: {e}")
    raise

# Crear carpeta de base de datos si no existe
os.makedirs(os.path.dirname(db_path), exist_ok=True)

# Cargar a SQLite
try:
    conn = sqlite3.connect(db_path)
    df.to_sql("studies", conn, if_exists="replace", index=False)
    conn.execute("CREATE INDEX IF NOT EXISTS idx_nct_number ON studies(nct_number);")
    logging.info("Datos cargados en SQLite con éxito.")
    logging.info("Índice creado en columna 'nct_number'.")
except Exception as e:
    logging.error(f"Error al cargar datos en SQLite: {e}")
    raise
finally:
    conn.close()
    logging.info("Conexión cerrada correctamente.")
