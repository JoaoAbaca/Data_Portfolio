# 💳 CoinGecko ETL Pipeline

Este proyecto implementa un pipeline de extracción, transformación y carga (ETL) utilizando Python y SQLite para procesar información de criptomonedas desde la API de CoinGecko. El objetivo es construir un flujo robusto y escalable que simule procesos típicos de un Data Engineer.

---

## 🌟 Objetivo

Simular un entorno real de procesamiento de datos utilizando prácticas profesionales de ingeniería de datos, incluyendo:

* Extracción de datos desde una API pública (CoinGecko)
* Validación y transformación de datos en bruto
* Persistencia en base de datos relacional (SQLite)
* Logging y manejo de errores

---

## 🧱 Estructura del proyecto

```
coin_gecko_pipeline/
│
├── extract.py          # Extrae datos desde la API de CoinGecko
├── transform.py        # Limpia y normaliza los datos extraídos
├── load.py             # Carga los datos transformados en una base SQLite
│
├── data/
│   ├── coin_data_raw.json        # Datos crudos extraídos desde la API
│   ├── coin_data_clean.csv       # CSV limpio con los datos procesados
│   └── coin_data.db              # Base de datos SQLite con la tabla final
│
└── README.md           # Documentación del proyecto
```

---

## 🔍 Datos utilizados

Se utiliza el endpoint `coins/markets` de la API pública de [CoinGecko](https://www.coingecko.com/en/api/documentation):

* Top 100 criptomonedas por capitalización de mercado
* Datos clave: nombre, símbolo, precio actual, volumen, market cap, cambio porcentual diario, etc.
* Formato original: JSON

---

## ⚙️ Requisitos

* Python 3.8+
* Paquetes:

  * `pandas`
  * `requests`
  * `sqlite3` (incluido por defecto)
  * `os`, `json`, `logging`

Instalar dependencias:

```bash
pip install pandas requests
```

---

## 🚀 Ejecución del pipeline

1. **Extraer los datos**:

```bash
python extract.py
```

2. **Transformar y limpiar**:

```bash
python transform.py
```

3. **Cargar a la base SQLite**:

```bash
python load.py
```

---

## 🧐 Lecciones aplicadas

✔ Buenas prácticas de codificación (PEP8, separación de etapas)
✔ Manejo de errores y validaciones robustas
✔ Uso de logs para trazabilidad
✔ Normalización y limpieza de datos reales
✔ Persistencia en base de datos relacional

---

## 📌 Autor

Joao — [Data Developer Portfolio](https://github.com/joaov-dev)
Proyecto 3 de 3 para postulación a Mutt Data (2025)

---
