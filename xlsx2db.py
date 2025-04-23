import pandas as pd
import sqlite3

domains = pd.read_excel("C:/Users/ayujo/SPRING2025/IST402/Research Goal FINAL.xlsx", sheet_name=None)
sqlitedb="DomainAssetsVul"

conn = sqlite3.connect(f"{sqlitedb}.db")
cursor = conn.cursor()

for domain, df in domains.items():
    # Create a table for each domain
    df.to_sql(domain, conn, if_exists='replace', index=False)
    print(f"Table {domain} created successfully.")

conn.close()