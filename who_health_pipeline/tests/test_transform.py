# tests/test_transform.py

import os
import pandas as pd
import pytest
from src.extract_data import extract_data
from src.validate_data import validate_data
from src.transform_data import transform_data
from src.transform_data import OUTPUT_PATH as TRANSFORMED_PATH

def test_transform_data(tmp_path):
    # Paths temporales
    raw_path = tmp_path / "raw.json"
    validated_path = tmp_path / "validated.csv"
    transformed_pa_
