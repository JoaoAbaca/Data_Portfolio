# 🪙 Crypto ETL Pipeline with Apache Airflow & Docker

This project implements an ETL (Extract - Transform - Load) pipeline using the CoinGecko API (https://www.coingecko.com/en/api) to obtain up-to-date cryptocurrency market information. The workflow is orchestrated with Apache Airflow and executed within Docker containers, ensuring portability, isolation, and ease of deployment.

---

## 🚀 What does this project do?

1. Extract: Downloads the main cryptoassets from the CoinGecko public API.
2. Transform: Cleans, filters, and normalizes the data, generating a structured CSV.
3. Load: Inserts the transformed data into a SQLite database.

All of this is executed as a DAG in Airflow, deployed via Docker Compose.

---

## 📂 Project Structure

crypto_etl_airflow/
├── dags/ # Airflow DAGs
│ └── crypto_etl_dag.py
├── scripts/ # ETL scripts in Python
│ ├── extract.py
│ ├── transform.py
│ └── load.py
├── data/ # Generated files (JSON, CSV, DB)
│ ├── raw/
│ └── processed/
├── docker-compose.yml # Service orchestration
├── Dockerfile # Base image (optional)
├── requirements.txt
└── README.md
---

## 🛠️ Technologies Used

- **Python 3.10**
- **Apache Airflow 2.8**
- **Docker & Docker Compose**
- **Pandas**
- **SQLite**
- **CoinGecko API**

---
## 🧪 How to run the project

### 1. Clone the repository

git clone https://github.com/JoaoAbaca/crypto_etl_airflow.git
cd crypto_etl_airflow

### 2. Initialize Airflow (only the first time)

docker-compose run airflow-webserver airflow db init
docker-compose run airflow-webserver airflow users create \
--username admin --firstname Joao --lastname Dev \
--role Admin --email joao@example.com --password admin

### 3. Start Airflow

docker-compose up

### 4. Access the web interface

Navigate to: http://localhost:8080

Username: admin

Password: admin

### 5. Run the DAG manually

Activate the crypto_etl_pipeline DAG from the interface

Click ▶️ to run it

View the results in the data/ folder

## 📌 Key Learnings

How to create a professional ETL environment using Docker containers

First contact with Apache Airflow as a data orchestrator

Modular separation of the pipeline into actual extraction, transformation, and loading stages

Project structure and documentation best practices