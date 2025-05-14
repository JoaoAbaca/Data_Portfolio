# 🧱 Proyecto ETL de Criptomonedas con Airflow, Docker y PostgreSQL

Este proyecto implementa un pipeline de ETL (Extracción, Transformación y Carga) sobre datos de criptomonedas en tiempo real. Está orquestado con Apache Airflow, contenerizado con Docker y almacena los datos en una base PostgreSQL.

---

## 🧠 Objetivo

Simular un entorno de producción donde se automatiza diariamente la recolección, validación, transformación y almacenamiento de datos desde una API externa. Este pipeline sirve como demostración técnica para el rol de Data Developer.

---

## ⚙️ Tecnologías utilizadas

- **Python 3.8**
- **Apache Airflow 2.8.1**
- **Docker & Docker Compose**
- **PostgreSQL 13**
- **Pandas / Pandera** (validación)
- **SQLAlchemy**
- **Pytest** (testing)

---

## 📊 Arquitectura del pipeline
API de CoinGecko
↓
[Extract] → Guarda JSON en data/raw/
↓
[Transform] → Limpieza, selección de columnas, validación con Pandera
↓
[Load] → Inserta en PostgreSQL usando SQLAlchemy


Orquestado con Airflow → `extract_data` → `transform_data` → `load_data`

---

## 🚧 Evolución del proyecto

| Versión | Descripción |
|---------|-------------|
| 🔹 **Inicial** | Scripts separados (`extract.py`, `transform.py`, `load.py`) con datos en local (JSON/CSV) y carga en SQLite |
| 🔹 **Mejoras** | Airflow para orquestación diaria, Pandera para validación, Docker para portabilidad, PostgreSQL para entorno realista, y tests con Pytest |

---

## 🧪 Testing

El proyecto incluye un test básico con `pytest` que valida:
- Que la transformación genere un archivo `.csv`
- Que las columnas estén completas
- Que no existan valores nulos

📁 Ubicación: `tests/test_transform.py`

---

## 🚀 ¿Cómo correr el proyecto?

### 1. Clonar el repositorio

```bash
git clone https://github.com/tuusuario/crypto-etl-airflow.git
cd crypto-etl-airflow

2. Build de Docker

docker-compose build --no-cache

3. Inicializar Airflow (solo la primera vez)

docker-compose run airflow-webserver airflow db init
docker-compose run airflow-webserver airflow users create \
  --username admin --firstname Joao --lastname Dev \
  --role Admin --email joao@example.com --password admin

4. Levantar los servicios

docker-compose up

Accedé a Airflow en: http://localhost:8080

Usuario: admin
Contraseña: admin
📂 Estructura de carpetas

crypto_etl_airflow/
├── dags/                  # DAG de Airflow
├── scripts/               # Scripts extract/transform/load
├── tests/                 # Pytest
├── data/                  # Datos en crudo y procesados (ignorado por Git)
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md

🛑 Exclusiones en .gitignore

data/
logs/
*.db
__pycache__/
*.pyc
.env
.vscode/
.idea/

📌 Observaciones

    El pipeline usa un endpoint limitado (top 10 criptos en USD), por lo que genera pocos registros por día.

    Ideal para demostrar habilidades en orquestación, contenerización, validación y automatización.

    Puede escalarse fácilmente con otras APIs o múltiples endpoints si se desea mayor volumen.

👨‍💻 Autor

Joao — Data Developer en formación
Proyecto de portafolio técnico orientado a roles de ingeniería de datos.


---

