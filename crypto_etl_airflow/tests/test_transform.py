import os
import sys
import pandas as pd

# Agregar scripts/ al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))

from transform import transform_crypto_data

def test_transform_creates_valid_csv():
    csv_path = transform_crypto_data()
    assert os.path.exists(csv_path), "El archivo CSV no fue creado"

    df = pd.read_csv(csv_path)

    expected_columns = [
        "id", "symbol", "name",
        "current_price", "market_cap",
        "total_volume", "last_updated"
    ]

    assert list(df.columns) == expected_columns, "Columnas incorrectas"
    assert len(df) > 0, "El archivo está vacío"
    assert df.isnull().sum().sum() == 0, "Hay valores nulos"
