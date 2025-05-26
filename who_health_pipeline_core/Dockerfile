FROM apache/airflow:2.9.1

# Copy requirements.txt
COPY requirements.txt .

# We install packages as the airflow user (recommended)
USER airflow

RUN pip install --no-cache-dir -r requirements.txt
