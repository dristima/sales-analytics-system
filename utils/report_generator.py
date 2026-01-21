import os
from datetime import datetime
from collections import defaultdict

def generate_sales_report(transactions, enriched_transactions, output_file='output/sales_report.txt'):
    """
    Generates a comprehensive formatted text report.
    """

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # HEADER
    generation_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total_records = len(transactions)

    # OVERALL SUMMARY
    total_revenue = sum(t['Quantity'] * t['UnitPrice'] for t in transactions)
    total_transactions = len(transactions)
    avg_order_value = total_revenue / total_transactions if total_transactions else 0
    dates = sorted(set(t['Date'] for t in transactions))
    date_range = f"{dates[0]} to {dates[-1]}" if dates else "N/A"

    # REGION-WISE PERFORMANCE
    region_stats = defaultdict(lambda: {"sales": 0, "count": 0})
    for t in transactions:
        region_stats[t['Region']]["sales"] += t['Quantity'] * t['UnitPrice']
        region_stats[t['Region']]["count"] += 1
    total_sales = sum(r["sales"] for r in region_stats.values())
    region_summary = sorted(region_stats.items(), key=lambda x: x[1]["sales"], reverse=True)

    # TOP 5 PRODUCTS
    product_stats = defaultdict(lambda: {"qty": 0, "revenue": 0})
    for t in transactions:
        product_stats[t['ProductName']]["qty"] += t['Quantity']
        product_stats[t['ProductName']]["revenue"] += t['Quantity'] * t['UnitPrice']
    top_products = sorted(product_stats.items(), key=lambda x: x[1]["qty"], reverse=True)[:5]

    # TOP 5 CUSTOMERS
    customer_stats = defaultdict(lambda: {"spent": 0, "orders": 0})
    for t in transactions:
        customer_stats[t['CustomerID']]["spent"] += t['Quantity'] * t['UnitPrice']
        customer_stats[t['CustomerID']]["orders"] += 1
    top_customers = sorted(customer_stats.items(), key=lambda x: x[1]["spent"], reverse=True)[:5]

    # DAILY SALES TREND
    daily_stats = defaultdict(lambda: {"revenue": 0, "transactions": 0, "customers": set()})
    for t in transactions:
        daily_stats[t['Date']]["revenue"] += t['Quantity'] * t['UnitPrice']
        daily_stats[t['Date']]["transactions"] += 1
        daily_stats[t['Date']]["customers"].add(t['CustomerID'])
    daily_summary = sorted(daily_stats.items())

    # PRODUCT PERFORMANCE ANALYSIS
    best_day = max(daily_summary, key=lambda x: x[1]["revenue"])[0] if daily_summary else "N/A"
    low_products = [(p, stats["qty"], stats["revenue"]) for p, stats in product_stats.items() if stats["qty"] < 10]
    avg_txn_per_region = {region: stats["sales"]/stats["count"] if stats["count"] else 0 for region, stats in region_stats.items()}

    # API ENRICHMENT SUMMARY
    enriched_count = len(enriched_transactions)
    success_rate = (enriched_count / len(product_stats)) * 100 if product_stats else 0
    failed_products = [p for p in product_stats.keys() if p not in enriched_transactions]

    # WRITE REPORT
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("============================================\n")
        f.write("           SALES ANALYTICS REPORT\n")
        f.write(f"         Generated: {generation_time}\n")
        f.write(f"         Records Processed: {total_records}\n")
        f.write("============================================\n\n")

        f.write("OVERALL SUMMARY\n")
        f.write("--------------------------------------------\n")
        f.write(f"Total Revenue:        ₹{total_revenue:,.2f}\n")
        f.write(f"Total Transactions:   {total_transactions}\n")
        f.write(f"Average Order Value:  ₹{avg_order_value:,.2f}\n")
        f.write(f"Date Range:           {date_range}\n\n")

        f.write("REGION-WISE PERFORMANCE\n")
        f.write("--------------------------------------------\n")
        f.write("Region    Sales         % of Total  Transactions\n")
        for region, stats in region_summary:
            pct = (stats["sales"]/total_sales)*100 if total_sales else 0
            f.write(f"{region:<8} ₹{stats['sales']:,.0f}   {pct:5.2f}%      {stats['count']}\n")
        f.write("\n")

        f.write("TOP 5 PRODUCTS\n")
        f.write("--------------------------------------------\n")
        f.write("Rank  Product Name        Quantity  Revenue\n")
        for i, (product, stats) in enumerate(top_products, 1):
            f.write(f"{i:<5} {product:<18} {stats['qty']:<8} ₹{stats['revenue']:,.0f}\n")
        f.write("\n")

        f.write("TOP 5 CUSTOMERS\n")
        f.write("--------------------------------------------\n")
        f.write("Rank  Customer ID   Total Spent   Orders\n")
        for i, (cust, stats) in enumerate(top_customers, 1):
            f.write(f"{i:<5} {cust:<12} ₹{stats['spent']:,.0f}   {stats['orders']}\n")
        f.write("\n")

        f.write("DAILY SALES TREND\n")
        f.write("--------------------------------------------\n")
        f.write("Date        Revenue       Transactions   Unique Customers\n")
        for date, stats in daily_summary:
            f.write(f"{date:<10} ₹{stats['revenue']:,.0f}   {stats['transactions']:<12} {len(stats['customers'])}\n")
        f.write("\n")

        f.write("PRODUCT PERFORMANCE ANALYSIS\n")
        f.write("--------------------------------------------\n")
        f.write(f"Best Selling Day: {best_day}\n")
        if low_products:
            f.write("Low Performing Products:\n")
            for p, qty, rev in low_products:
                f.write(f"  {p}: Quantity={qty}, Revenue=₹{rev:,.0f}\n")
        else:
            f.write("No low performing products.\n")
        f.write("Average Transaction Value per Region:\n")
        for region, avg in avg_txn_per_region.items():
            f.write(f"  {region}: ₹{avg:,.2f}\n")
        f.write("\n")

        f.write("API ENRICHMENT SUMMARY\n")
        f.write("--------------------------------------------\n")
        f.write(f"Total Products Enriched: {enriched_count}\n")
        f.write(f"Success Rate: {success_rate:.2f}%\n")
        if failed_products:
            f.write("Products not enriched:\n")
            for p in failed_products:
                f.write(f"  {p}\n")
        else:
            f.write("All products enriched successfully.\n")
            