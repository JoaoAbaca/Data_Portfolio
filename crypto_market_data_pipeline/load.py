import pandas as pd
import sqlite3
import os
import logging

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(message)s'
)

# Rutas
csv_path = "data/coin_data_clean.csv"
db_path = "data/coin_data.db"

# Verificar existencia del archivo CSV
if not os.path.exists(csv_path):
    logging.error(f"El archivo CSV no existe: {csv_path}")
    exit()

# Leer CSV limpio
try:
    df = pd.read_csv(csv_path)
    logging.info(f"Archivo CSV cargado: {csv_path}")
    logging.info(f"Registros a cargar: {len(df)}")
except Exception as e:
    logging.error(f"Error al leer el archivo CSV: {e}")
    exit()

# Crear carpeta si no existe
os.makedirs(os.path.dirname(db_path), exist_ok=True)

# Cargar en SQLite
try:
    conn = sqlite3.connect(db_path)
    df.to_sql("coins", conn, if_exists="replace", index=False)

    # Crear índice para mejorar performance
    with conn:
        conn.execute("CREATE INDEX IF NOT EXISTS idx_coin_id ON coins(id);")

    logging.info(f"Datos cargados en la base de datos: {db_path}")
    logging.info("Índice creado en la columna 'id'")
except Exception as e:
    logging.error(f"Error al cargar los datos en la base: {e}")
finally:
    conn.close()
    logging.info("Conexión a la base cerrada.")
