import pandas as pd
import sqlite3
import os


def load_to_sqlite():
    # Find the most recent CSV file in data/processed
    processed_dir = os.path.join("data", "processed")
    files = sorted(
        [f for f in os.listdir(processed_dir) if f.endswith(".csv")],
        reverse=True
    )

    if not files:
        raise FileNotFoundError("No .csv files were found in data/processed")

    csv_file = os.path.join(processed_dir, files[0])
    df = pd.read_csv(csv_file)

    # Create connection to SQLite
    conn = sqlite3.connect("crypto_data.db")

    # Save to table called 'market_data''
    df.to_sql("market_data", conn, if_exists="append", index=False)

    conn.close()
    print(f"✅ Data loaded into SQLite database from {csv_file}")

# Execute directly if this script is run
if __name__ == "__main__":
    load_to_sqlite()
