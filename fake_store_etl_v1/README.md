# Fake Store ETL Pipeline

Este proyecto implementa un pipeline de Extracción, Transformación y Carga (ETL) utilizando datos de la API pública de [Fake Store](https://fakestoreapi.com/), orientado al desarrollo de habilidades clave para un rol de Data Developer.

## Objetivo

Diseñar y ejecutar un pipeline de datos robusto para extraer información de productos, usuarios y pedidos desde una API REST, transformarla y almacenarla en una base de datos relacional.

## Tecnologías utilizadas

* Python 3.10+
* Requests
* Pandas
* SQLite3
* JSON

## Estructura del Proyecto

```
fake_store_pipeline/
├── data/                     # Archivos intermedios y base de datos
│   ├── products_raw.json
│   ├── products_clean.csv
│   ├── fake_store.db
│   
├── extract.py               # Extracción de datos desde la API
├── transform.py             # Limpieza y normalización de datos
├── load.py                  # Carga de datos a SQLite
├── README.md
├── requirements.txt
└── .gitignore
```

## Pipeline ETL

### Extracción (`extract.py`)

* Descarga datos desde la API de Fake Store:

  * Productos: `/products`
  * Usuarios: `/users`
  * Pedidos: `/carts`
* Guarda los datos en formato JSON.

### Transformación (`transform.py`)

* Normaliza los datos de productos:

  * Convierte estructuras anidadas (como `rating`) en columnas planas.
  * Establece tipos de datos consistentes.
  * Elimina duplicados.
  * Guarda los datos en formato CSV.

### Carga (`load.py`)

* Carga los datos limpios a una base de datos SQLite:

  * Crea la tabla `products`.
  * Inserta los registros desde el CSV transformado.
  * Crea un índice sobre la columna `id` para mejorar consultas.

## Ejecución del pipeline

```bash
# Paso 1: Extracción
python extract.py

# Paso 2: Transformación
python transform.py

# Paso 3: Carga
python load.py
```

## Mejores prácticas implementadas

* Validación de estructura de datos.
* Separación clara por etapa (ETL).
* Trazabilidad mediante impresión de logs simples.
* Uso de SQLite para almacenamiento estructurado.
* Manejo de errores en la etapa de carga.

## Mejoras futuras

* Soporte para usuarios y pedidos en el pipeline.
* Pruebas unitarias para validación de transformaciones.
* Logging estructurado.
* Automatización mediante cron o workflows.

## Autor

Joao — [LinkedIn](https://www.linkedin.com/in/joaogithub)
