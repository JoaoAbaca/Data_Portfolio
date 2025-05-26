# src/extract_data.py

import os
import requests
import pandas as pd

# Directory where the downloaded data will be stored
RAW_DATA_DIR = "data/raw"
os.makedirs(RAW_DATA_DIR, exist_ok=True)

# Dictionary with the indicator codes and the relevant columns to keep
tables_info = {
    "WHOSIS_000001": ["IndicatorCode", "SpatialDim", "ParentLocation", "Dim1", "TimeDim", "NumericValue", "High", "Low"],
    "UHC_INDEX_REPORTED": ["IndicatorCode", "SpatialDim", "ParentLocation", "TimeDim", "NumericValue"],
    # Previously considered, but later excluded due to redundancy or data limitations:
    # "SRHINSTITUTIONALBIRTH": [...]
    "WSH_WATER_SAFELY_MANAGED": ["IndicatorCode", "SpatialDim", "ParentLocation", "Dim1", "TimeDim", "NumericValue"],
    "WSH_SANITATION_SAFELY_MANAGED": ["IndicatorCode", "SpatialDim", "ParentLocation", "Dim1", "TimeDim", "NumericValue"]
}

def extract_table(table_code, columns):
    """
    Downloads a table from the WHO API and stores the selected columns in a CSV file.

    Args:
        table_code (str): The WHO API table code.
        columns (list): List of columns to retain from the downloaded dataset.
    """
    url = f"https://ghoapi.azureedge.net/api/{table_code}"
    print(f"Downloading {table_code}...")
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error downloading {table_code}: {response.status_code}")
        return

    data = response.json().get("value", [])
    if not data:
        print(f"No data available for {table_code}.")
        return

    df = pd.DataFrame(data)
    df = df[columns]  # Filter to keep only relevant columns

    output_path = os.path.join(RAW_DATA_DIR, f"{table_code}.csv")
    df.to_csv(output_path, index=False)
    print(f"{table_code} saved to {output_path}.")

def main():
    """
    Main function that iterates over all tables and triggers the extraction.
    """
    for table_code, columns in tables_info.items():
        extract_table(table_code, columns)

if __name__ == "__main__":
    main()
