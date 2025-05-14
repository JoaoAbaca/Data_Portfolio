import pandas as pd
import json
import os
import logging

# Configure logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Entry and exit routes
input_path = "data/raw/products.json"
output_path = "data/processed/products_clean.csv"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

def cargar_datos():
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"File not found: {input_path}")

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("The JSON file does not contain a list of products.")

    return data

def transformar_datos(data):
    df = pd.DataFrame(data)

    # Normalize the 'rating' column (which is a dict)
    if "rating" in df.columns:
        rating_df = pd.json_normalize(df["rating"])
        rating_df.columns = ["rating_rate", "rating_count"]
        df = df.drop(columns=["rating"]).join(rating_df)

    # Validate expected columns
    columnas_esperadas = {'id', 'title', 'price', 'description', 'category', 'image', 'rating_rate', 'rating_count'}
    if not columnas_esperadas.issubset(df.columns):
        raise ValueError(f"Missing expected columns: {columnas_esperadas - set(df.columns)}")

    # Basic cleaning
    df.drop_duplicates(subset="id", inplace=True)
    df.dropna(subset=["title", "price", "category"], inplace=True)

    # Optional normalization
    df["title"] = df["title"].str.strip()
    df["category"] = df["category"].str.strip().str.lower()

    return df

def guardar_datos(df):
    df.to_csv(output_path, index=False)
    logging.info(f"✅ Transformed data saved in: {output_path}")

def main():
    try:
        logging.info("🔄 Starting data transformation...")
        data = cargar_datos()
        df = transformar_datos(data)
        guardar_datos(df)
    except Exception as e:
        logging.error(f"❌ Error in transformation: {e}")

if __name__ == "__main__":
    main()
