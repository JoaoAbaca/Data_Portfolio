# 🧱 Cryptocurrency ETL Project with Airflow, Docker, and PostgreSQL

This project implements an ETL pipeline (Extract, Transform, Load) for real-time cryptocurrency data. It is orchestrated using Apache Airflow, containerized with Docker, and stores the data in a PostgreSQL database.

---

## 🧠 Objective

Simulate a production environment that automates daily data extraction, validation, transformation, and loading from an external API. This pipeline serves as a technical demonstration for a Data Developer role.

---

## ⚙️ Technologies Used

- **Python 3.8**
- **Apache Airflow 2.8.1**
- **Docker & Docker Compose**
- **PostgreSQL 13**
- **Pandas / Pandera** (data validation)
- **SQLAlchemy**
- **Pytest** (testing)

---

## 📊 Pipeline Architecture

CoinGecko API  
↓  
**Extract:** Saves JSON files in `data/raw/`  
↓  
**Transform:** Cleans data, selects columns, validates with Pandera  
↓  
**Load:** Inserts data into PostgreSQL using SQLAlchemy  

Orchestrated by Airflow: `extract_data` → `transform_data` → `load_data`

---

## 🚧 Project Evolution

| Version   | Description                                                          |
|-----------|----------------------------------------------------------------------|
| 🔹 Initial | Separate scripts (`extract.py`, `transform.py`, `load.py`) saving data locally (JSON/CSV) and loading into SQLite |
| 🔹 Improvements | Added Airflow for daily orchestration, Pandera for validation, Docker for portability, PostgreSQL for realistic environment, and Pytest for automated testing |

---

## 🧪 Testing

Includes basic `pytest` tests to verify:  
- CSV file is generated after transformation  
- Columns are complete and correct  
- No null values present  

Test location: `tests/test_transform.py`

---

## 🚀 How to Run the Project

### 1. Clone the repository

bash
git clone https://github.com/yourusername/crypto-etl-airflow.git
cd crypto-etl-airflow

### 2. Build Docker images
docker-compose build --no-cache

### 3. Initialize Airflow database (first-time setup)
docker-compose run airflow-webserver airflow db init
docker-compose run airflow-webserver airflow users create \
  --username admin --firstname Joao --lastname Dev \
  --role Admin --email joao@example.com --password admin

### 4. Start all services
docker-compose up
Access Airflow UI at: http://localhost:8080
Username: admin
Password: admin

### 📂 Folder Structure
crypto_etl_airflow/
├── dags/                  # Airflow DAG definitions
├── scripts/               # Extract, Transform, Load scripts
├── tests/                 # Pytest tests
├── data/                  # Raw and processed data (ignored by Git)
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md

### 🛑 Git Ignore Rules
data/
logs/
*.db
__pycache__/
*.pyc
.env
.vscode/
.idea/

### 📌 Notes
* The pipeline uses a limited API endpoint (top 10 cryptocurrencies by market cap in USD), so it produces a small dataset daily.

* Ideal to showcase skills in orchestration, containerization, validation, and automation.

* Easily scalable to include more APIs or larger datasets.

### 👨‍💻 Author
Joao — Aspiring Data Developer
Technical portfolio project targeting Data  roles.