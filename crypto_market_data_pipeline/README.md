# 💳 CoinGecko ETL Pipeline

This project implements an extract, transform, and load (ETL) pipeline using Python and SQLite to process cryptocurrency data from the CoinGecko API. The goal is to build a robust and scalable workflow that simulates typical data engineering processes.

---

## 🌟 Objective

Simulate a real-world data processing environment using professional data engineering practices, including:

* Extracting data from a public API (CoinGecko)
* Validating and transforming raw data
* Persistence in a relational database (SQLite)
* Logging and error handling

---

## 🧱 Project Structure

```
coin_gecko_pipeline/
│
├── extract.py # Extract data from the CoinGecko API
├── transform.py # Cleanse and normalize extracted data
├── load.py # Load transformed data into a SQLite database
│
├── data/
│ ├── coin_data_raw.json # Raw data extracted from the API
│ ├── coin_data_clean.csv # Cleaned CSV with the processed data
│ └── coin_data.db # SQLite database with the final table
│
└── README.md # Project documentation
```

---

## 🔍 Data used

The `coins/markets` endpoint of the [CoinGecko](https://www.coingecko.com/en/api/documentation) is used:

* Top 100 cryptocurrencies by market capitalization
* Key data: name, symbol, current price, volume, market cap, daily percentage change, etc.
* Original format: JSON

---

## ⚙️ Requirements

* Python 3.8+
* Packages:

* `pandas`
* `requests`
* `sqlite3` (included by default)
* `os`, `json`, `logging`

Install dependencies:

```bash
pip install pandas requests
```

---

## 🚀 Executing the pipeline

1. **Extract the data**:

```bash
python extract.py
```

2. **Transform and clean**:

```bash
python transform.py
```

3. **Load to the SQLite database**:

```bash
python load.py
```

---

## 🧐 Applied lessons

✔ Good coding practices (PEP8, stage separation)
✔ Error handling and robust validation
✔ Use of logs for traceability
✔ Normalization and cleansing of real data
✔ Persistence in relational databases

---

## 📌 Author

Joao — [Data Developer Portfolio](https://github.com/joaov-dev)
Project 3 of 3 for Mutt Data application (2025)

---