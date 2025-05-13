# 🪙 Crypto ETL Pipeline with Apache Airflow & Docker

Este proyecto implementa un pipeline **ETL (Extract - Transform - Load)** utilizando [CoinGecko API](https://www.coingecko.com/en/api) para obtener información actualizada del mercado de criptomonedas. El flujo de trabajo es orquestado con **Apache Airflow** y ejecutado dentro de contenedores **Docker**, lo que garantiza portabilidad, aislamiento y facilidad de despliegue.

---

## 🚀 ¿Qué hace este proyecto?

1. **Extract**: Descarga los principales criptoactivos desde la API pública de CoinGecko.
2. **Transform**: Limpia, filtra y normaliza los datos, generando un CSV estructurado.
3. **Load**: Inserta los datos transformados en una base de datos SQLite.

Todo esto se ejecuta como un **DAG en Airflow**, desplegado vía Docker Compose.

---

## 📂 Estructura del proyecto

crypto_etl_airflow/
├── dags/ # DAG de Airflow
│ └── crypto_etl_dag.py
├── scripts/ # Scripts ETL en Python
│ ├── extract.py
│ ├── transform.py
│ └── load.py
├── data/ # Archivos generados (JSON, CSV, DB)
│ ├── raw/
│ └── processed/
├── docker-compose.yml # Orquestación de servicios
├── Dockerfile # Imagen base (opcional)
├── requirements.txt
└── README.md


---

## 🛠️ Tecnologías usadas

- **Python 3.10**
- **Apache Airflow 2.8**
- **Docker & Docker Compose**
- **Pandas**
- **SQLite**
- **CoinGecko API**

---

## 🧪 Cómo ejecutar el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/JoaoAbaca/crypto_etl_airflow.git
cd crypto_etl_airflow

2. Inicializar Airflow (solo la primera vez)

docker-compose run airflow-webserver airflow db init
docker-compose run airflow-webserver airflow users create \
  --username admin --firstname Joao --lastname Dev \
  --role Admin --email joao@example.com --password admin

3. Levantar Airflow

docker-compose up

4. Acceder a la interfaz web

    Navegar a: http://localhost:8080

    Usuario: admin

    Contraseña: admin

5. Ejecutar el DAG manualmente

    Activar el DAG crypto_etl_pipeline desde la interfaz

    Clic en ▶️ para correrlo

    Ver los resultados en la carpeta data/

    📌 Aprendizajes clave

    Cómo crear un entorno ETL profesional usando contenedores Docker

    Primer contacto con Apache Airflow como orquestador de datos

    Separación modular del pipeline en etapas reales de extracción, transformación y carga

    Buenas prácticas de estructura y documentación de proyectos