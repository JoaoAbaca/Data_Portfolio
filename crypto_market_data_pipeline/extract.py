# extract.py

import requests
import os
import json
from datetime import datetime

# Create folder for data if it does not exist
os.makedirs("data", exist_ok=True)

# Define parameters for the API
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1,
    "sparkline": False
}

#Make a request
response = requests.get(url, params=params)

# Validate response
if response.status_code == 200:
    data = response.json()

    # Save result to file
    timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = f"data/raw_coin_data.json"

    with open(output_file, "w") as f:
        json.dump(data, f, indent=2)

    print(f"✅ Data extracted and saved in: {output_file}")
else:
    print(f"❌ Error in the request: {response.status_code}")
