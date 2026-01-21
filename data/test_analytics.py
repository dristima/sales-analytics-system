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

    # Top products
    top_products = top_selling_products(valid, n=5)
    print("\n=== Top Selling Products ===")
    for product, qty, revenue in top_products:
        print(f"{product}: Quantity={qty}, Revenue={revenue}")

    # Customer analysis
    customer_summary = customer_analysis(valid)
    print("\n=== Customer Analysis ===")
    for customer, stats in customer_summary.items():
        print(f"{customer}: {stats}")

    # Daily sales trend
    daily_summary = daily_sales_trend(valid)
    print("\n=== Daily Sales Trend ===")
    for date, stats in daily_summary.items():
        print(f"{date}: {stats}")

    # Peak sales day
    peak_day = find_peak_sales_day(valid)
    print("\n=== Peak Sales Day ===")
    print(peak_day)

    # Low performing products
    low_products = low_performing_products(valid, threshold=10)
    print("\n=== Low Performing Products ===")
    for product, qty, revenue in low_products:
        print(f"{product}: Quantity={qty}, Revenue={revenue}")

    # API calls
    products, total = fetch_products(limit=100)
    print(f"Total products available: {total}")
    print(f"Products fetched: {len(products)}")

    for p in products[:5]:
        print(f"{p['id']}: {p['title']} - ${p['price']}")

    product = fetch_product_by_id(1)
    print("=== Single Product ===")
    print(f"{product['id']}: {product['title']}")

    results = search_products("phone")
    print(f"Products found: {len(results)}")
    for p in results:
        print(f"{p['id']}: {p['title']} - ${p['price']}")

    # Report generation
    enriched_transactions = [p['title'] for p in products]  # placeholder enrichment
    generate_sales_report(valid, enriched_transactions)

    print("✅ Sales report generated at output/sales_report.txt")

if __name__ == "__main__":
    main()