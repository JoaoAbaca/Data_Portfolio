import json
import pandas as pd
import os

# Definir rutas
raw_path = "data/raw_coin_data.json"
output_path = "data/coin_data_clean.csv"

# Verificar que el archivo existe
if not os.path.exists(raw_path):
    raise FileNotFoundError(f"❌ Archivo JSON no encontrado: {raw_path}")

# Cargar datos
with open(raw_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Crear DataFrame
df = pd.DataFrame(data)

# Seleccionar columnas de interés
columns_needed = [
    "id", "symbol", "name", "current_price", "market_cap", "market_cap_rank",
    "total_volume", "price_change_percentage_24h", "circulating_supply", "last_updated"
]

df = df[columns_needed]

# Renombrar columnas a snake_case
df.columns = [col.lower().strip().replace(" ", "_") for col in df.columns]

# Convertir columna de fecha a tipo datetime
df["last_updated"] = pd.to_datetime(df["last_updated"], errors="coerce")

# Eliminar registros con valores faltantes críticos
df.dropna(subset=["id", "current_price", "market_cap"], inplace=True)

# Guardar como CSV limpio
df.to_csv(output_path, index=False)
print(f"✅ Transformación completa. Archivo guardado en: {output_path}")
