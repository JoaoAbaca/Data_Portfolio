# Fake Store ETL Pipeline

This project implements an Extract, Transform, and Load (ETL) pipeline using data from the [Fake Store](https://fakestoreapi.com/) public API, aimed at developing key skills for a Data Developer role.

## Objective

Design and implement a robust data pipeline to extract product, user, and order information from a REST API, transform it, and store it in a relational database.

## Technologies Used

* Python 3.10+
* Requests
* Pandas
* SQLite3
* JSON

## Project Structure

```
fake_store_pipeline/
├── data/ # Intermediate files and database
│ ├── products_raw.json
│ ├── products_clean.csv
│ ├── fake_store.db
│
├── extract.py # Extracting data from the API
├── transform.py # Data cleansing and normalization
├── load.py # Loading data into SQLite
├── README.md
├── requirements.txt
└── .gitignore
```

## ETL Pipeline

### Extraction (`extract.py`)

* Download data from the Fake Store API:

* Products: `/products`
* Users: `/users`
* Orders: `/carts`
* Save data in JSON format.

### Transformation (`transform.py`)

* Normalize product data:

* Convert nested structures (such as `rating`) into flat columns.
* Set consistent data types.
* Remove duplicates.
* Save data in CSV format.

### Load (`load.py`)

* Load the cleaned data into a SQLite database:

* Create the `products` table.
* Insert records from the transformed CSV.
* Create an index on the `id` column to improve queries.

## Pipeline Execution

```bash
# Step 1: Extraction
python extract.py

# Step 2: Transformation
python transform.py

# Step 3: Loading
python load.py
```

## Best Practices Implemented

* Data structure validation.
* Clear separation by stage (ETL).
* Traceability through simple log printing.
* Use of SQLite for structured storage.
* Error handling in the loading stage.

## Future Enhancements

* Support for users and orders in the pipeline.
* Unit tests for transformation validation.
* Structured logging.
* Automation through cron or workflows.

## Author

Joao — [LinkedIn](https://www.linkedin.com/in/joaogithub)