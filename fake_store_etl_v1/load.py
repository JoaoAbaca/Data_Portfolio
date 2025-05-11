import pandas as pd
import sqlite3
import os
import logging

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Rutas
csv_path = "data/processed/products_clean.csv"
db_path = "data/fake_store.db"
table_name = "products"

# Asegurar carpeta
os.makedirs(os.path.dirname(db_path), exist_ok=True)

def cargar_csv(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"No se encuentra el archivo CSV: {path}")
    
    df = pd.read_csv(path)
    if df.empty:
        raise ValueError("El archivo CSV está vacío.")

    logging.info(f"📄 CSV cargado con {len(df)} registros.")
    return df

def cargar_a_sqlite(df, db_path, table_name):
    try:
        conn = sqlite3.connect(db_path)
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        
        # Crear índice
        with conn:
            conn.execute(f"CREATE INDEX IF NOT EXISTS idx_product_id ON {table_name}(id);")
        
        logging.info(f"✅ Datos cargados en SQLite '{db_path}', tabla '{table_name}'.")
        logging.info(f"📌 Índice creado en columna 'id'.")
    except Exception as e:
        logging.error(f"❌ Error al cargar datos en SQLite: {e}")
    finally:
        conn.close()
        logging.info("🔒 Conexión cerrada.")

def main():
    try:
        logging.info("🚀 Iniciando carga de datos a SQLite...")
        df = cargar_csv(csv_path)
        cargar_a_sqlite(df, db_path, table_name)
    except Exception as e:
        logging.error(f"❌ Error general en la carga: {e}")

if __name__ == "__main__":
    main()
