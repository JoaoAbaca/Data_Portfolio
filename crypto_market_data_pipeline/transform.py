import pandas as pd
import logging
import os

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(message)s'
)

# Rutas
raw_path = "data/coin_data_raw.json"
clean_path = "data/coin_data_clean.csv"

# Verificar existencia del archivo
if not os.path.exists(raw_path):
    logging.error(f"No se encontró el archivo de entrada: {raw_path}")
    exit()

# Cargar JSON
try:
    df = pd.read_json(raw_path)
    logging.info(f"Archivo cargado: {raw_path}")
except Exception as e:
    logging.error(f"Error al leer JSON: {e}")
    exit()

# Ver columnas disponibles
expected_cols = [
    'id', 'symbol', 'name', 'current_price', 'market_cap',
    'market_cap_rank', 'total_volume', 'high_24h', 'low_24h',
    'price_change_percentage_24h', 'last_updated'
]
df = df[expected_cols]

# Validación de datos
original_count = len(df)

# Eliminar filas con nulos en campos clave
df.dropna(subset=['id', 'symbol', 'name', 'current_price'], inplace=True)

# Validar que ciertos campos sean positivos
df = df[df['current_price'] > 0]
df = df[df['market_cap_rank'] > 0]

filtered_count = len(df)
logging.info(f"Filas originales: {original_count} | Filas limpias: {filtered_count}")

# Guardar CSV limpio
df.to_csv(clean_path, index=False)
logging.info(f"Datos transformados guardados en: {clean_path}")
