import os
import json
import pandas as pd
from datetime import datetime
from glob import glob
import pandera as pa
from pandera import Column, DataFrameSchema


def get_latest_json_file(raw_dir="data/raw/"):
    json_files = glob(os.path.join(raw_dir, "*.json"))
    if not json_files:
        raise FileNotFoundError("No JSON files were found in data/raw/")
    latest_file = max(json_files, key=os.path.getctime)
    return latest_file


# Define the expected validation scheme
schema = DataFrameSchema({
    "id": Column(str),
    "symbol": Column(str),
    "name": Column(str),
    "current_price": Column(float),
    "market_cap": Column(float),
    "total_volume": Column(float),
    "last_updated": Column(str),
})


def transform_crypto_data():
    # Get latest JSON file
    input_file = get_latest_json_file()
    with open(input_file, "r") as f:
        data = json.load(f)

    # Load to DataFrame
    df = pd.DataFrame(data)

    # Select relevant columns
    df_clean = df[[
        "id", "symbol", "name",
        "current_price", "market_cap",
        "total_volume", "last_updated"
    ]].copy()

    # Convert numeric columns to float to ensure schema compatibility
    num_cols = ["current_price", "market_cap", "total_volume"]
    df_clean[num_cols] = df_clean[num_cols].astype(float)

    # Validate data
    schema.validate(df_clean)

    # Create output folder if it does not exist
    output_dir = "data/processed"
    os.makedirs(output_dir, exist_ok=True)

    # Save CSV with timestamp
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(output_dir, f"crypto_data_clean_{timestamp}.csv")
    df_clean.to_csv(output_file, index=False)

    print(f"✅ Transformed and validated data. File saved in {output_file}")
    return output_file


if __name__ == "__main__":
    transform_crypto_data()
