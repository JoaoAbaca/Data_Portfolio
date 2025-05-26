# src/transform_data.py

import pandas as pd
from pathlib import Path

# Define directories
RAW_DIR = Path("data/validated")  # Use validated data
PROCESSED_DIR = Path("data/processed")
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# Load country codes table
country_codes = pd.read_csv("data/raw/country_codes.csv")
country_codes = country_codes.rename(columns={"alpha-3": "country_code", "name": "country_name"})

# Optional mappings
SEX_MAPPING = {"MLE": "Male", "FMLE": "Female", "BTSX": "Both sexes"}
RESIDENCE_MAPPING = {"RUR": "Rural", "URB": "Urban", "TOTAL": "Total"}

def clean_common(df, indicator_name, has_dim1=False, has_high_low=False, dim1_type="sex"):
    """
    Standardize and clean common columns for all datasets.
    """
    df = df.rename(columns={
        "IndicatorCode": f"{indicator_name.lower()}_code",
        "SpatialDim": "country_code",
        "ParentLocation": "region",
        "TimeDim": "year",
        "NumericValue": f"{indicator_name.lower()}_value"
    })

    if has_high_low:
        df = df.rename(columns={
            "High": f"{indicator_name.lower()}_high",
            "Low": f"{indicator_name.lower()}_low"
        })

    if has_dim1:
        df = df.rename(columns={"Dim1": "dim1"})
        if dim1_type == "sex":
            df["dim1"] = df["dim1"].map(SEX_MAPPING).fillna(df["dim1"])
        elif dim1_type == "residence":
            df["dim1"] = df["dim1"].map(RESIDENCE_MAPPING).fillna(df["dim1"])

    df["year"] = pd.to_numeric(df["year"], errors="coerce")
    df = df.dropna(subset=["year", "country_code"])
    df = df.drop_duplicates()
    df["indicator_name"] = indicator_name

    return df

def pivot_indicator(df, indicator_name):
    """
    Pivot Dim1 values (sex or residence) into separate columns.
    """
    pivot = df.pivot_table(
        index=["country_code", "year"],
        columns="dim1",
        values=f"{indicator_name}_value"
    ).reset_index()

    pivot.columns.name = None
    pivot = pivot.rename(columns={
        "Both sexes": f"{indicator_name}_total",
        "Male": f"{indicator_name}_male",
        "Female": f"{indicator_name}_female",
        "Rural": f"{indicator_name}_rural",
        "Urban": f"{indicator_name}_urban",
        "Total": f"{indicator_name}_total"
    })
    return pivot

def transform_all():
    datasets = {
        "WHOSIS_000001": {"name": "life_expectancy", "has_dim1": True, "has_high_low": True, "dim1_type": "sex"},
        "UHC_INDEX_REPORTED": {"name": "uhc_index", "has_dim1": False, "has_high_low": False},
        "WSH_WATER_SAFELY_MANAGED": {"name": "water_access", "has_dim1": True, "has_high_low": False, "dim1_type": "residence"},
        "WSH_SANITATION_SAFELY_MANAGED": {"name": "sanitation_access", "has_dim1": True, "has_high_low": False, "dim1_type": "residence"}
    }

    minimal_country_codes = country_codes[["country_code", "country_name"]]

    for raw_name, config in datasets.items():
        file_path = RAW_DIR / f"{raw_name}.csv"
        df = pd.read_csv(file_path)
        df_clean = clean_common(
            df,
            indicator_name=config["name"],
            has_dim1=config.get("has_dim1", False),
            has_high_low=config.get("has_high_low", False),
            dim1_type=config.get("dim1_type", "sex")
        )

        # Pivot if needed
        if config.get("has_dim1"):
            df_clean = pivot_indicator(df_clean, config["name"])

            # Impute missing values where possible
            total_col = f"{config['name']}_total"
            urban_col = f"{config['name']}_urban"
            rural_col = f"{config['name']}_rural"

            if total_col in df_clean.columns:
                # Estimate total from average if missing
                df_clean[total_col] = df_clean[total_col].fillna(
                    df_clean[[urban_col, rural_col]].mean(axis=1)
                )

                # Estimate urban if missing
                df_clean[urban_col] = df_clean[urban_col].fillna(
                    (2 * df_clean[total_col]) - df_clean[rural_col]
                )

                # Estimate rural if missing
                df_clean[rural_col] = df_clean[rural_col].fillna(
                    (2 * df_clean[total_col]) - df_clean[urban_col]
                )

        # Add country names and primary key
        df_clean = df_clean.merge(minimal_country_codes, how="left", on="country_code")
        df_clean["pk_country_year"] = df_clean["country_code"] + "_" + df_clean["year"].astype(int).astype(str)

        # Save processed file
        df_clean.to_csv(PROCESSED_DIR / f"{config['name']}.csv", index=False)

    print("Transformations complete. Individual files saved to 'data/processed'.")

if __name__ == "__main__":
    transform_all()
