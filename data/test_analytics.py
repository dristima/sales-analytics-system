from utils.file_handler import read_sales_data
from utils.parser import parse_transactions
from utils.validator import validate_and_filter
from utils.data_processor import calculate_total_revenue, region_wise_sales
from utils.data_processor import top_selling_products

def main():
    # Step 1: Read raw data
    raw_lines = read_sales_data("data/sales_data.txt")

    # Step 2: Parse into structured transactions
    transactions = parse_transactions(raw_lines)

    # Step 3: Validate and filter
    valid, invalid_count, summary = validate_and_filter(
        transactions, region="South", min_amount=500
    )

    # Step 4: Calculate total revenue
    total_revenue = calculate_total_revenue(valid)
    print("\n=== Total Revenue ===")
    print(total_revenue)

    # Step 5: Region-wise sales breakdown
    region_summary = region_wise_sales(valid)
    print("\n=== Region-wise Sales ===")
    for region, stats in region_summary.items():
        print(f"{region}: {stats}")

    top_products = top_selling_products(valid, n=5)
    print("\n=== Top Selling Products ===")
    for product, qty, revenue in top_products:
        print(f"{product}: Quantity={qty}, Revenue={revenue}")

if __name__ == "__main__":
    main()