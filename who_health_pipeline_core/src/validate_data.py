# src/validate_data.py

import pandas as pd
from pathlib import Path

# Directories
RAW_DIR = Path("data/raw")
VALIDATED_DIR = Path("data/validated")
VALIDATED_DIR.mkdir(parents=True, exist_ok=True)

# Expected schema for each table
tables_schema = {
    "WHOSIS_000001": ["IndicatorCode", "SpatialDim", "ParentLocation", "Dim1", "TimeDim", "NumericValue", "High", "Low"],
    "UHC_INDEX_REPORTED": ["IndicatorCode", "SpatialDim", "ParentLocation", "TimeDim", "NumericValue"],
    "WSH_WATER_SAFELY_MANAGED": ["IndicatorCode", "SpatialDim", "ParentLocation", "Dim1", "TimeDim", "NumericValue"],
    "WSH_SANITATION_SAFELY_MANAGED": ["IndicatorCode", "SpatialDim", "ParentLocation", "Dim1", "TimeDim", "NumericValue"]
}

def validate_table(file_name, expected_columns):
    file_path = RAW_DIR / f"{file_name}.csv"
    if not file_path.exists():
        print(f"{file_name} not found.")
        return

    df = pd.read_csv(file_path)

    # Check for missing columns
    missing_columns = [col for col in expected_columns if col not in df.columns]
    if missing_columns:
        print(f"{file_name} is missing columns: {missing_columns}")
        return

    # Basic type conversions
    if "TimeDim" in df.columns:
        df["TimeDim"] = pd.to_numeric(df["TimeDim"], errors="coerce")

    if "NumericValue" in df.columns:
        df["NumericValue"] = pd.to_numeric(df["NumericValue"], errors="coerce")

    if "High" in df.columns:
        df["High"] = pd.to_numeric(df["High"], errors="coerce")

    if "Low" in df.columns:
        df["Low"] = pd.to_numeric(df["Low"], errors="coerce")

    # Remove duplicates
    df = df.drop_duplicates()

    # Save validated file
    df.to_csv(VALIDATED_DIR / f"{file_name}.csv", index=False)
    print(f"{file_name} validated and saved to {VALIDATED_DIR}")

def main():
    for table, expected_columns in tables_schema.items():
        validate_table(table, expected_columns)

if __name__ == "__main__":
    main()
