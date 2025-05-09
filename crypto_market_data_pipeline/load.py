import pandas as pd
import sqlite3
import os

# Rutas
csv_path = "data/coin_data_clean.csv"
db_path = "data/crypto_market.db"

# Verificar existencia del archivo CSV
if not os.path.exists(csv_path):
    raise FileNotFoundError(f"❌ Archivo CSV no encontrado: {csv_path}")

# Leer CSV
df = pd.read_csv(csv_path)
print(f"[INFO] CSV leído: {len(df)} registros.")

# Crear carpeta si no existe
os.makedirs(os.path.dirname(db_path), exist_ok=True)

# Conectar a SQLite y cargar los datos
try:
    conn = sqlite3.connect(db_path)
    df.to_sql("market_data", conn, if_exists="replace", index=False)

    # Crear índices útiles
    with conn:
        conn.execute("CREATE INDEX IF NOT EXISTS idx_coin_id ON market_data(id);")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_market_cap_rank ON market_data(market_cap_rank);")

    print(f"✅ Datos cargados en '{db_path}', tabla 'market_data'.")
    print("🗂️  Índices creados en 'id' y 'market_cap_rank'.")

except Exception as e:
    print(f"❌ Error durante carga: {e}")

finally:
    conn.close()
    print("[INFO] Conexión cerrada.")
