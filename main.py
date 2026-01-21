from utils.file_handler import read_sales_data
from utils.parser import parse_transactions
from utils.validator import validate_and_filter
from utils.data_processor import (
    calculate_total_revenue,
    region_wise_sales,
    top_selling_products,
    customer_analysis,
    daily_sales_trend,
    find_peak_sales_day,
    low_performing_products,
)
from utils.api_handler import fetch_products, fetch_product_by_id, search_products
from utils.report_generator import generate_sales_report


def main():
    # === STEP 1: Load and parse local sales data ===
    raw_lines = read_sales_data("data/sales_data.txt")
    transactions = parse_transactions(raw_lines)

    # === STEP 2: Validate and filter ===
    valid_transactions, invalid_count, summary = validate_and_filter(
        transactions, region="South", min_amount=500
    )

    # === STEP 3: Analytics ===
    total_revenue = calculate_total_revenue(valid_transactions)
    region_summary = region_wise_sales(valid_transactions)
    top_products = top_selling_products(valid_transactions, n=5)
    customer_summary = customer_analysis(valid_transactions)
    daily_summary = daily_sales_trend(valid_transactions)
    peak_day = find_peak_sales_day(valid_transactions)
    low_products = low_performing_products(valid_transactions, threshold=10)

    # === STEP 4: API Enrichment ===
    products, total = fetch_products(limit=100)
    enriched_transactions = [p['title'] for p in products]  # placeholder enrichment

    # === STEP 5: Generate Report ===
    generate_sales_report(valid_transactions, enriched_transactions)

    print("✅ Sales report generated at output/sales_report.txt")


if __name__ == "__main__":
    main()