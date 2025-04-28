import pandas as pd
import sqlite3

# Read all sheets into a dictionary of DataFrames
domains = pd.read_excel("C:/Users/ayujo/SPRING2025/IST402/Research Goal FINAL.xlsx", sheet_name=None)

# Create a new empty list to collect all data
all_data = []

# Go through each sheet (domain)
for domain, df in domains.items():
    df['DomainName'] = domain  # Optional: add a column to know which domain it came from
    all_data.append(df)

# Combine all DataFrames together into one
combined_df = pd.concat(all_data, ignore_index=True)

# Now save it into ONE table
sqlitedb = "DomainAssetsVul"
conn = sqlite3.connect(f"project-src/database/{sqlitedb}.db")
cursor = conn.cursor()

# Save combined data into a single table (e.g., 'AllDomains')
combined_df.to_sql('AllDomains', conn, if_exists='replace', index=False)

print("All data combined into table 'AllDomains' successfully.")

conn.close()
