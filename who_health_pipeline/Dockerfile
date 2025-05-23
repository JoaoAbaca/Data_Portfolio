FROM apache/airflow:2.9.1

# Copiamos requirements.txt
COPY requirements.txt .

# Instalamos paquetes como el usuario airflow (recomendado)
USER airflow

RUN pip install --no-cache-dir -r requirements.txt
