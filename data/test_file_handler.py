import sys
import os

# Add parent folder to Python path so "utils" can be found
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.file_handler import read_sales_data

records = read_sales_data("data/sales_data.txt")
print(f"Total records loaded: {len(records)}")
print("First 3 records:")
for line in records[:3]:
    print(line)
