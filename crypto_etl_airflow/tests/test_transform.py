import os
import sys
import pandas as pd

# Add scripts/ to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))

from transform import transform_crypto_data

def test_transform_creates_valid_csv():
    csv_path = transform_crypto_data()
    assert os.path.exists(csv_path), "The CSV file was not created"
    df = pd.read_csv(csv_path)

    expected_columns = [
        "id", "symbol", "name",
        "current_price", "market_cap",
        "total_volume", "last_updated"
    ]

    assert list(df.columns) == expected_columns, "Incorrect columns"
    assert len(df) > 0, "The file is empty"
    assert df.isnull().sum().sum() == 0, "There are null values"
