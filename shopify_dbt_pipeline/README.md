# Proyecto ETL y Data Warehouse con Airflow, DBT y PostgreSQL

Este proyecto implementa un pipeline completo de extracción, transformación y carga (ETL) para datos de ventas, utilizando tecnologías modernas de ingeniería de datos: **Airflow**, **DBT**, y **PostgreSQL**. El objetivo es construir un esquema en estrella para análisis de ventas, con tablas de hechos y dimensiones, listo para alimentar dashboards y sistemas de BI.

---

## Contenido

- Extracción de datos desde APIs o archivos
- Transformación y limpieza con Python y DBT
- Orquestación con Apache Airflow
- Almacenamiento en base de datos PostgreSQL
- Modelado dimensional para análisis (fact y dimensiones)
- Visualización con vistas resumen preparadas para BI

---

## Estructura del proyecto

project_root/
├── dags/ # DAGs de Airflow para orquestar el pipeline
├── data/ # Datos en bruto (raw), como archivos .xlsx
├── dbt/ # Proyecto DBT con modelos SQL y configuraciones
│ └── sales_dbt/
│ ├── models/
│ │ ├── staging/ # Modelos staging (limpieza y normalización)
│ │ ├── dim_*.sql # Tablas de dimensiones (productos, países, fechas...)
│ │ ├── fact_orders.sql # Tabla de hechos de ventas
│ │ └── sales_summary.sql # Vista resumen agregada para BI
│ ├── dbt_project.yml
│ └── schema.yml # Documentación y tests DBT
├── scripts/ # Scripts Python para extracción y carga inicial
├── Dockerfile # Imagen base para contenedores con dependencias
├── docker-compose.yml # Orquestación de servicios (Airflow + PostgreSQL)
└── requirements.txt # Librerías Python necesarias


---

## Flujo de trabajo

1. **Extracción**: Se extraen datos de APIs o archivos y se cargan en PostgreSQL en tablas crudas (`raw_orders`).
2. **Transformación inicial (staging)**: DBT limpia y normaliza datos creando vistas staging (`stg_orders`).
3. **Modelado dimensional**: DBT crea tabla de hechos (`fact_orders`) y tablas de dimensiones (`dim_product_type`, `dim_country`, etc.).
4. **Agregación y resumen**: DBT genera vistas resumen (`sales_summary`) para análisis rápidos y dashboards.
5. **Orquestación**: Apache Airflow coordina la ejecución automática y periódica del pipeline.

---

## Tecnologías usadas

- **Python** para scripting ETL y automatización
- **Apache Airflow** para orquestación y scheduling
- **DBT (Data Build Tool)** para modelado y transformación SQL
- **PostgreSQL** como base de datos relacional y data warehouse
- **Docker** y **Docker Compose** para ambientes reproducibles y aislados

---

## Cómo usar este proyecto

### Prerrequisitos

- Docker y Docker Compose instalados
- Acceso a terminal con bash

### Pasos

1. Clonar este repositorio

2. Construir e iniciar los contenedores

bash    Entrar al contenedor Airflow webserver para comandos DBT

docker-compose run airflow-webserver bash

    Ejecutar DBT para compilar modelos

cd /opt/airflow/dbt/sales_dbt
dbt run

    Acceder a Airflow en el navegador: http://localhost:8080

    Explorar tablas y vistas en PostgreSQL (ejemplo con psql)

psql -h localhost -U airflow -d airflow
SELECT * FROM dbt_joao.sales_summary LIMIT 10;

### 3 Estructura de modelos DBT

    stg_orders.sql: limpieza y estandarización de columnas

    fact_orders.sql: tabla de hechos con ventas

    dim_*: tablas de dimensiones (producto, cliente, fecha, país, método de pago)

    sales_summary.sql: tabla agregada lista para análisis y dashboards

### 4 Próximos pasos / Mejoras

    Añadir más dimensiones (cliente, producto detallado, promociones)

    Implementar tests DBT automáticos para calidad de datos

    Integrar pipeline con dashboards en Power BI o Streamlit

    Añadir procesamiento incremental para grandes volúmenes

    Explorar integración con ML para forecasting y recomendaciones

### 5 Contacto

Para dudas o sugerencias, contactame:
Joao — [tu-email@example.com] — [LinkedIn/GitHub]
docker-compose up --build
