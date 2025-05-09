import pandas as pd
import os
import logging

# Configurar logging
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "transform.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(log_file, mode='a'),
        logging.StreamHandler()
    ]
)

# Rutas
input_csv = "C:/Users/User/Desktop/Data_Portfolio/clinical_trials_pipeline/data/studies_clean.csv"
output_csv = "C:/Users/User/Desktop/Data_Portfolio/clinical_trials_pipeline/data/studies_transform.csv"

# Verificar archivo de entrada
if not os.path.exists(input_csv):
    logging.error(f"Archivo de entrada no encontrado: {input_csv}")
    raise FileNotFoundError(f"❌ No se encuentra el archivo CSV: {input_csv}")

# Transformaciones
try:
    df = pd.read_csv(input_csv)
    logging.info("Archivo cargado correctamente para transformación.")

    # Seleccionar columnas
    cols = ['NCT Number', 'Study Title', 'Study Status', 'Conditions',
            'Interventions', 'Sex', 'Age', 'Phases', 'Study Type', 'Locations']
    df = df[cols]
    df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]

    # Eliminar duplicados
    df.drop_duplicates(subset=['nct_number', 'study_title'], inplace=True)

    # Eliminar filas sin título
    df.dropna(subset=['study_title'], inplace=True)

    # Separar y explotar condiciones
    df['conditions'] = df['conditions'].astype(str).str.split('|')
    df = df.explode('conditions')
    df['conditions'] = df['conditions'].str.strip()

    # Separar y explotar intervenciones
    df['interventions'] = df['interventions'].astype(str).str.split('|')
    df = df.explode('interventions')
    df['interventions'] = df['interventions'].str.strip()

    # Separar y explotar fases
    df['phases'] = df['phases'].astype(str).str.replace('PHASE', '', regex=False)
    df['phases'] = df['phases'].str.split('|')
    df = df.explode('phases')
    df['phases'] = df['phases'].str.strip()
    df['phases'] = df['phases'].apply(lambda x: f"Phase {x}" if x else None)

    # Separar edades
    df['age'] = df['age'].astype(str).str.split(',')
    df = df.explode('age')
    df['age'] = df['age'].str.strip()

    # Guardar
    df.to_csv(output_csv, index=False)
    logging.info(f"Transformación completada. Archivo guardado en: {output_csv}")
    logging.info(f"Registros finales: {len(df)}")

except Exception as e:
    logging.error(f"Error durante transformación: {e}")
    raise
