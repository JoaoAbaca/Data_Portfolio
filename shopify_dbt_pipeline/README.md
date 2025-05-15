# 📁 Shopify Sales Analytics with DBT and PostgreSQL

This project implements a data transformation pipeline using DBT (Data Build Tool) to process sales data from an Excel file structured like Shopify data, loading it into a PostgreSQL database, orchestrated via Docker.

---

## 🧾 Dataset

The `orders.xlsx` file contains sales records including customer info, products, prices, payment methods, and dates.

---

## 🛠️ Tools Used

- **PostgreSQL 13:** relational storage for raw and transformed data  
- **DBT 1.8.7:** transformation, dimensional modeling, and data quality validation  
- **Docker & Docker Compose:** reproducible and isolated environment  
- **Pandas:** initial loading of the Excel file into the database  
- **SQLAlchemy:** programmatic connection to PostgreSQL  

---

## 🔁 Pipeline Flow

orders.xlsx (Excel)
↓
load_excel_to_postgres.py
↓
PostgreSQL (raw_orders table)
↓
DBT (stg_orders → dim_* and fact_orders → sales_summary)


---

## 📦 Folder Structure

shopify_dbt_pipeline/
├── data/
│ └── orders.xlsx
├── dbt/
│ └── sales_dbt/
│ ├── models/
│ │ ├── staging/
│ │ │ └── stg_orders.sql
│ │ ├── dim_date.sql
│ │ ├── dim_country.sql
│ │ ├── dim_city.sql
│ │ ├── dim_customer.sql
│ │ ├── dim_product_type.sql
│ │ ├── dim_gateway.sql
│ │ ├── fact_orders.sql
│ │ ├── sales_summary.sql
│ │ └── schema.yml
│ └── dbt_project.yml
├── scripts/
│ └── load_excel_to_postgres.py
├── dags/ (optional)
├── docker-compose.yml
├── requirements.txt
└── README.md


---

## ✅ How to Run the Pipeline

1. Clone the repository and navigate to the project root

bash
git clone <repo_url>
cd shopify_dbt_pipeline

2. Build the Docker containers

docker-compose build

3. Initialize Airflow database (if using Airflow)

docker-compose run airflow-webserver airflow db init

4. Start all services

docker-compose up

5. Load raw data into PostgreSQL
Inside the webserver container:
docker exec -it <webserver_container_name> bash
python scripts/load_excel_to_postgres.py
(Example if using default container name:) docker exec -it shopify_dbt_pipeline-airflow-webserver-1 bash

6. Inside the container:
cd /opt/airflow/dbt/sales_dbt
dbt debug       # optional: check connection and config
dbt run         # run all models
dbt test        # run tests defined in schema.yml

### 🧪 Validations
The schema.yml file defines 15+ automatic tests, including:

    not_null and unique for primary keys or key fields

    Data integrity checks for columns such as total_price_usd, invoice_date, country, product_type, etc.

### 🧠 Why This Project?

Versioning and lineage managed by DBT

Clear separation of raw, staging, and analytical models

Automated data quality validations

Production-ready, reproducible environment with Docker


### 👨‍💻 Author
Joao — Aspiring Data Developer
Technical portfolio project targeting Data  roles.