import os
import json
import pandas as pd
import pandera as pa
from pandera import Column, DataFrameSchema

# Rutas por defecto
RAW_DATA_PATH = os.path.join("data", "raw_data.json")
VALIDATED_DATA_PATH = os.path.join("data", "validated_data.csv")

# Esquema reducido
schema = DataFrameSchema({
    "IndicatorCode": Column(str),
    "SpatialDim": Column(str),
    "ParentLocation": Column(str, nullable=True),
    "TimeDim": Column(int),
    "NumericValue": Column(float, nullable=True),
    "Low": Column(float, nullable=True),
    "High": Column(float, nullable=True),
    "Dim1": Column(str, nullable=True),
})

def validate_data(raw_path: str = RAW_DATA_PATH, output_path: str = VALIDATED_DATA_PATH):
    try:
        with open(raw_path, "r", encoding="utf-8") as f:
            raw_json = json.load(f)

        records = raw_json.get("value", [])
        df = pd.DataFrame(records)

        print("Primeras 5 filas:")
        print(df.head())
        print("\nColumnas disponibles:", df.columns.tolist())

        # Filtramos solo columnas del esquema
        df = df[list(schema.columns)]

        validated_df = schema.validate(df)
        print("Datos validados correctamente.")

        validated_df.to_csv(output_path, index=False)
        print(f"Datos guardados en: {output_path}")

    except FileNotFoundError:
        print(f"Archivo no encontrado: {raw_path}")
    except pa.errors.SchemaError as e:
        print("Error de validación del esquema:", e)
    except Exception as ex:
        print("Error inesperado:", ex)

if __name__ == "__main__":
    validate_data()
