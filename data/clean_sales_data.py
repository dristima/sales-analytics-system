import pandas as pd

# Load raw TXT file (pipe-delimited)
df = pd.read_csv("data/sales_data.txt", sep="|")

# Drop empty lines
df.dropna(how="all", inplace=True)

# Track total records parsed
total_records = len(df)

# Clean ProductName (remove commas)
df["ProductName"] = df["ProductName"].str.replace(",", " ", regex=False)

# Clean UnitPrice (remove commas, convert to numeric)
df["UnitPrice"] = df["UnitPrice"].astype(str).str.replace(",", "", regex=False)
df["UnitPrice"] = pd.to_numeric(df["UnitPrice"], errors="coerce")

# Define validity rules
valid_ids = df["TransactionID"].astype(str).str.startswith("T")
valid_quantity = df["Quantity"] > 0
valid_price = df["UnitPrice"] > 0
valid_customer = df["CustomerID"].notna()
valid_region = df["Region"].notna()

# Apply rules
df_clean = df[valid_ids & valid_quantity & valid_price & valid_customer & valid_region]

# Count invalid records
invalid_records = total_records - len(df_clean)

# Save cleaned data
df_clean.to_csv("cleaned_sales_data.csv", index=False)

# Print summary
print(f"Total records parsed: {total_records}")
print(f"Invalid records removed: {invalid_records}")
print(f"Valid records after cleaning: {len(df_clean)}")

from utils.file_handler import read_sales_data
from utils.parser import parse_transactions

raw_lines = read_sales_data("data/sales_data.txt")
cleaned_records = parse_transactions(raw_lines)

print(f"Parsed {len(cleaned_records)} valid transactions")
print("First 3 records:")
for r in cleaned_records[:3]:
    print(r)