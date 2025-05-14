import pandas as pd
import sqlite3
import os
import logging

# # Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Path
csv_path = "data/processed/products_clean.csv"
db_path = "data/fake_store.db"
table_name = "products"

#Secure folder
os.makedirs(os.path.dirname(db_path), exist_ok=True)

def cargar_csv(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"CSV file not found: {path}")
    
    df = pd.read_csv(path)
    if df.empty:
        raise ValueError("The CSV file is empty.")

    logging.info(f"📄 CSV loaded with {len(df)} records.")
    return df

def cargar_a_sqlite(df, db_path, table_name):
    try:
        conn = sqlite3.connect(db_path)
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        
        # Create index
        with conn:
            conn.execute(f"CREATE INDEX IF NOT EXISTS idx_product_id ON {table_name}(id);")
        
        logging.info(f"✅ Data loaded into SQLite '{db_path}', table '{table_name}'.")
        logging.info(f"📌 Index created on column 'id'.")
    except Exception as e:
        logging.error(f"❌ Error loading data into SQLite: {e}")
    finally:
        conn.close()
        logging.info("🔒Connection closed.")

def main():
    try:
        logging.info("🚀 Starting data loading to SQLite...")
        df = cargar_csv(csv_path)
        cargar_a_sqlite(df, db_path, table_name)
    except Exception as e:
        logging.error(f"❌ General error in loading: {e}")

if __name__ == "__main__":
    main()
