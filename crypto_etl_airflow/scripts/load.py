import pandas as pd
import sqlite3
import os


def load_to_sqlite():
    # Buscar el archivo CSV más reciente en data/processed
    processed_dir = os.path.join("data", "processed")
    files = sorted(
        [f for f in os.listdir(processed_dir) if f.endswith(".csv")],
        reverse=True
    )

    if not files:
        raise FileNotFoundError("No se encontraron archivos .csv en data/processed")

    csv_file = os.path.join(processed_dir, files[0])
    df = pd.read_csv(csv_file)

    # Crear conexión a SQLite
    conn = sqlite3.connect("crypto_data.db")

    # Guardar en tabla llamada 'market_data'
    df.to_sql("market_data", conn, if_exists="append", index=False)

    conn.close()
    print(f"✅ Datos cargados en la base de datos SQLite desde {csv_file}")

# Ejecutar directamente si se corre este script
if __name__ == "__main__":
    load_to_sqlite()
