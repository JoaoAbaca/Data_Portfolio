import requests
import json
import os
from datetime import datetime


def extract_crypto_data():
    # Ensure that the 'data/raw' directory exists
    raw_dir = os.path.join("data", "raw")
    os.makedirs(raw_dir, exist_ok=True)

    # URL de la API
    url = "https://api.coingecko.com/api/v3/coins/markets"
    
    # Parameters to get the top 10 crypto assets
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1,
        "sparkline": False
    }

    # Make the request
    response = requests.get(url, params=params)
    data = response.json()

    # Create file name with timestamp
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(raw_dir, f"crypto_data_{timestamp}.json")

    # Save as JSON
    with open(output_path, "w") as f:
        json.dump(data, f, indent=4)

    print(f"✅ Data extracted and saved in{output_path}")
    return output_path  # <- important to use in ETL

# Execute directly if this script is run
if __name__ == "__main__":
    extract_crypto_data()
