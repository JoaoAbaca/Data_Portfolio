import pandas as pd
import sqlite3
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(message)s'
)

# Path
csv_path = "data/coin_data_clean.csv"
db_path = "data/coin_data.db"

# Check for the existence of the CSV file
if not os.path.exists(csv_path):
    logging.error(f"The CSV file does not exist: {csv_path}")
    exit()

# Read clean CSV
try:
    df = pd.read_csv(csv_path)
    logging.info(f"CSV file uploaded: {csv_path}")
    logging.info(f"Records to load: {len(df)}")
except Exception as e:
    logging.error(f"Error reading CSV file: {e}")
    exit()

# Create folder if it doesn't exist
os.makedirs(os.path.dirname(db_path), exist_ok=True)

# Load into SQLite
try:
    conn = sqlite3.connect(db_path)
    df.to_sql("coins", conn, if_exists="replace", index=False)

    # Create index to improve performance
    with conn:
        conn.execute("CREATE INDEX IF NOT EXISTS idx_coin_id ON coins(id);")

    logging.info(f"Data loaded into the database: {db_path}")
    logging.info("Index created on column 'id'")
except Exception as e:
    logging.error(f"Error loading data into the database: {e}")
finally:
    conn.close()
    logging.info("Connection to the closed base.")
