import pandas as pd
import logging
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(message)s'
)

# Path
raw_path = "data/raw_coin_data.json"
clean_path = "data/coin_data_clean.csv"

# Check for file existence
if not os.path.exists(raw_path):
    logging.error(f"The input file was not found.: {raw_path}")
    exit()

# Load JSON
try:
    df = pd.read_json(raw_path)
    logging.info(f"File uploaded: {raw_path}")
except Exception as e:
    logging.error(f"Error reading JSON: {e}")
    exit()

# View available columns
expected_cols = [
    'id', 'symbol', 'name', 'current_price', 'market_cap',
    'market_cap_rank', 'total_volume', 'high_24h', 'low_24h',
    'price_change_percentage_24h', 'last_updated'
]
df = df[expected_cols]

# Data validation
original_count = len(df)

# Delete rows with nulls in key fields
df.dropna(subset=['id', 'symbol', 'name', 'current_price'], inplace=True)

# Validate that certain fields are positive
df = df[df['current_price'] > 0]
df = df[df['market_cap_rank'] > 0]

filtered_count = len(df)
logging.info(f"Original rows: {original_count} | Clean rows: {filtered_count}")

# Save clean CSV
df.to_csv(clean_path, index=False)
logging.info(f"Transformed data saved in: {clean_path}")
