from scripts.extract import extract_crypto_data
from scripts.transform import transform_crypto_data
from scripts.load import load_to_sqlite

def run_etl():
    print("🔄 Iniciando pipeline ETL para datos de criptomonedas...")
    
    extract_crypto_data()
    transform_crypto_data()
    load_to_sqlite()
    
    print("✅ Pipeline ETL finalizado con éxito.")

if __name__ == "__main__":
    run_etl()
