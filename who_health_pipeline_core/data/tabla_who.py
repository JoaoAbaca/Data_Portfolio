import requests
import pandas as pd

# Paso 1: Descargar el JSON desde la API traducida
url = "https://ghoapi-azureedge-net.translate.goog/api/Indicator?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc"
response = requests.get(url)
data = response.json()

# Convertir la lista de indicadores a un DataFrame
df_api = pd.json_normalize(data['value'])

# Guardar a CSV opcionalmente
df_api.to_csv("indicadores_api.csv", index=False)

# Paso 2: Cargar el CSV local con las tablas descargadas previamente
df_who = pd.read_csv("tablas_who.csv")

# Paso 3: Realizar un join para quedarnos solo con los indicadores que realmente están disponibles
df_merged = df_who.merge(df_api, how="left", left_on="Name", right_on="IndicatorCode")

# Paso 4: Guardar el resultado final
df_merged.to_csv("tablas_descripciones.csv", index=False)

print("Archivo 'tablas_descripciones.csv' generado con éxito.")
