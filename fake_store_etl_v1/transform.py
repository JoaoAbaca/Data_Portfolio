import pandas as pd
import json
import os
import logging

# Configurar logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Rutas de entrada y salida
input_path = "data/raw/products.json"
output_path = "data/processed/products_clean.csv"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

def cargar_datos():
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"No se encuentra el archivo: {input_path}")

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("El archivo JSON no contiene una lista de productos.")

    return data

def transformar_datos(data):
    df = pd.DataFrame(data)

    # Normalizar la columna 'rating' (que es un dict)
    if "rating" in df.columns:
        rating_df = pd.json_normalize(df["rating"])
        rating_df.columns = ["rating_rate", "rating_count"]
        df = df.drop(columns=["rating"]).join(rating_df)

    # Validar columnas esperadas
    columnas_esperadas = {'id', 'title', 'price', 'description', 'category', 'image', 'rating_rate', 'rating_count'}
    if not columnas_esperadas.issubset(df.columns):
        raise ValueError(f"Faltan columnas esperadas: {columnas_esperadas - set(df.columns)}")

    # Limpieza básica
    df.drop_duplicates(subset="id", inplace=True)
    df.dropna(subset=["title", "price", "category"], inplace=True)

    # Normalización opcional
    df["title"] = df["title"].str.strip()
    df["category"] = df["category"].str.strip().str.lower()

    return df

def guardar_datos(df):
    df.to_csv(output_path, index=False)
    logging.info(f"✅ Datos transformados guardados en: {output_path}")

def main():
    try:
        logging.info("🔄 Iniciando transformación de datos...")
        data = cargar_datos()
        df = transformar_datos(data)
        guardar_datos(df)
    except Exception as e:
        logging.error(f"❌ Error en transformación: {e}")

if __name__ == "__main__":
    main()
