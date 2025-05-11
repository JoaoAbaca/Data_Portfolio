import requests
import pandas as pd
import sqlite3

# 1. Extract data from the API
url = "https://fakestoreapi.com/products"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"✅ Data obtained: {len(data)} productos.\n")
else:
    print("❌ Error connecting to the API:", response.status_code)
    data = []

# 2. Convert to DataFrame (normalize nested fields)
df = pd.json_normalize(data)
print("📊 Original DataFrame (first 3 records):")
print(df.head(3))
print("\n🔍 Original columns:")
print(df.columns.tolist())

# 3. Rename rating columns.
df.rename(columns={
    "rating.rate": "rate",
    "rating.count": "count"
}, inplace=True)

print("\n✅ Columns after renaming:")
print(df.columns.tolist())

# 4. Connect to SQLite and save
conn = sqlite3.connect("store.db")
df.to_sql("products", conn, if_exists="replace", index=False)

print("\n💾 Data stored in 'store.db' in the 'products' table'.")


# 5. Read the SQL file with the queries
with open("queries.sql", "r") as file:
    queries = file.read().strip().split(';')  # Split queries by the delimiter ';'

# Connecting to the database
conn = sqlite3.connect("store.db")

# 6. Execute each query and display the result
for query in queries:
    query = query.strip()  # Remove extra spaces
    if query:  # Ensure the query is not empty
        try:
            result = pd.read_sql_query(query, conn)
            print(result)  # Display query results
        except Exception as e:
            print(f"Error executing query: {e}")

# Close the connection
conn.close()