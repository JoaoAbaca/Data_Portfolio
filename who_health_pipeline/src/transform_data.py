import os
import pandas as pd

VALIDATED_DATA_PATH = os.path.join("data", "validated_data.csv")
TRANSFORMED_DATA_PATH = os.path.join("data", "transformed_data.csv")

def transform_data(input_path: str = VALIDATED_DATA_PATH, output_path: str = TRANSFORMED_DATA_PATH):
    try:
        df = pd.read_csv(input_path)
        print(f"Datos validados cargados: {df.shape[0]} filas")

        # Eliminar filas donde falte al menos uno de estos campos clave
        df_clean = df.dropna(subset=["IndicatorCode", "SpatialDim", "TimeDim", "NumericValue"])

        print(f"Datos transformados: {df_clean.shape[0]} filas después de eliminar nulos")

        df_clean.to_csv(output_path, index=False)
        print(f"Datos transformados guardados en: {output_path}")
    except Exception as e:
        print("Error al transformar los datos:", e)

if __name__ == "__main__":
    transform_data()
