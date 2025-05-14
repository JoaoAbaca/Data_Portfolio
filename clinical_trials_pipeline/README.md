# Clinical Trials ETL Pipeline

This repository contains an Extraction, Transformation, and Loading (ETL) pipeline for processing diabetes-related clinical trial data from ClinicalTrials.gov.

---

## 📊 Project Structure

```
clinical_trials_pipeline/
│
├── data/                        # Archivos de entrada/salida CSV y SQLite
│   ├── clinical_trials_diabetes.csv
│   ├── studies_clean.csv
│   ├── studies_transform.csv
│   
├── database/                   # Archivos de  SQLite
│   └── clinical_trials.db
├── src/                        # Logs de ejecución de los scripts
│   ├── extract.log
│   ├── transform.log
│   └── load.log
│   └── logs
│
└── README.md
```

---

## 🧰 Dataset 

* Source: ClinicalTrials.gov
* Topic: Diabetes Clinical Trials
* Original format: Manually exported CSV

---

## ⚖️ Description of the Scripts

### `extract.py`

* Reads the original file `Raw_Diabetes_Clinical_Trials.csv`
* Saves it as `studies_clean.csv`
* Includes error handling and logging

### `transform.py`

* Cleans, normalizes, and structures the data:

  * Renames columns to `snake_case`
  * Removes duplicates and nulls in `study_title`
  * Separates and explodes multiple values ​​into:

  * `conditions` (separated by `|`)
  * `interventions` (by `|`)
  * `phases` (by `|`, normalized as `Phase X`)
  * `age` (by `,`, e.g. `ADULT, OLDER_ADULT`)
* Saves the result as `studies_transform.csv`

### `load.py`

* Loads the transformed data into a SQLite database: `clinical_trials.db`
* Destination table: `studies`
* Creates an index on `nct_number`
* Includes full logging and error handling
---

## 🚀 Execution

Run in order from the project folder:

```bash
python extract.py
python transform.py
python load.py
```

Review the logs in the `logs/` folder to verify the success of each stage.

---

## 📊 Possible Improvements

* Unit tests with `pytest`
* Visualizations or final dashboard
* Added schema validations
* Automated data downloads from ClinicalTrials.gov

---

## 💼 Author

Joao — Portfolio project for Data Engineering vacancies.

---

## 📢 License

Uis personal and educational. ClinicalTrials.gov allows the use of your data for analytical purposes under certain terms.
