import matplotlib.pyplot as plt
from utils.file_handler import read_sales_data
from utils.parser import parse_transactions
from data.sales_analytics import compute_revenue, summarize_sales

def plot_revenue_by_product(summary):
    products = list(summary["RevenueByProduct"].keys())
    revenues = list(summary["RevenueByProduct"].values())

    plt.figure(figsize=(10, 6))
    plt.bar(products, revenues, color="skyblue")
    plt.xticks(rotation=45, ha="right")
    plt.title("Revenue by Product")
    plt.xlabel("Product")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.show()

def plot_revenue_by_region(summary):
    regions = list(summary["RevenueByRegion"].keys())
    revenues = list(summary["RevenueByRegion"].values())

    plt.figure(figsize=(6, 6))
    plt.pie(revenues, labels=regions, autopct="%1.1f%%", startangle=140)
    plt.title("Revenue Distribution by Region")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    raw_lines = read_sales_data("data/sales_data.txt")
    records = parse_transactions(raw_lines)
    records = compute_revenue(records)
    summary = summarize_sales(records)

    plot_revenue_by_product(summary)
    plot_revenue_by_region(summary)