def calculate_total_revenue(transactions):
    """
    Calculate total revenue from a list of transactions.
    """
    total_revenue = 0.0
    for t in transactions:
        try:
            qty = int(t.get("Quantity", 0))
            price = float(t.get("UnitPrice", 0.0))
            total_revenue += qty * price
        except (ValueError, TypeError):
            continue
    return total_revenue


def region_wise_sales(transactions):
    """
    Analyzes sales by region.
    Returns: dictionary with region statistics.
    """
    region_stats = {}
    total_sales_all = 0.0

    # Step 1: Aggregate sales and counts per region
    for t in transactions:
        try:
            qty = int(t.get("Quantity", 0))
            price = float(t.get("UnitPrice", 0.0))
            revenue = qty * price
            region = t.get("Region", "Unknown")

            if region not in region_stats:
                region_stats[region] = {"total_sales": 0.0, "transaction_count": 0}

            region_stats[region]["total_sales"] += revenue
            region_stats[region]["transaction_count"] += 1
            total_sales_all += revenue
        except (ValueError, TypeError):
            continue

    # Step 2: Calculate percentages
    for region, stats in region_stats.items():
        if total_sales_all > 0:
            stats["percentage"] = round((stats["total_sales"] / total_sales_all) * 100, 2)
        else:
            stats["percentage"] = 0.0

    # Step 3: Sort by total_sales in descending order
    sorted_stats = dict(
        sorted(region_stats.items(), key=lambda x: x[1]["total_sales"], reverse=True)
    )

    return sorted_stats


def top_selling_products(transactions, n=5):
    """
    Finds top n products by total quantity sold.

    Returns: list of tuples

    Expected Output Format:
    [
        ('Laptop', 45, 2250000.0),  # (ProductName, TotalQuantity, TotalRevenue)
        ('Mouse', 38, 19000.0),
        ...
    ]
    """
    product_stats = {}

    # Step 1: Aggregate by product
    for t in transactions:
        try:
            qty = int(t.get("Quantity", 0))
            price = float(t.get("UnitPrice", 0.0))
            revenue = qty * price
            product = t.get("ProductName", "Unknown")

            if product not in product_stats:
                product_stats[product] = {"total_qty": 0, "total_revenue": 0.0}

            product_stats[product]["total_qty"] += qty
            product_stats[product]["total_revenue"] += revenue
        except (ValueError, TypeError):
            continue

    # Step 2: Sort by total quantity sold (descending)
    sorted_products = sorted(
        product_stats.items(),
        key=lambda x: x[1]["total_qty"],
        reverse=True
    )

    # Step 3: Build result list of tuples
    top_products = [
        (product, stats["total_qty"], stats["total_revenue"])
        for product, stats in sorted_products[:n]
    ]

    return top_products   # ✅ fixed return


def customer_analysis(transactions):
    """
    Analyzes customer purchase patterns.

    Returns: dictionary of customer statistics
    """
    customer_stats = {}

    # Step 1: Aggregate stats per customer
    for t in transactions:
        try:
            customer_id = t.get("CustomerID", "Unknown")
            qty = int(t.get("Quantity", 0))
            price = float(t.get("UnitPrice", 0.0))
            revenue = qty * price
            product = t.get("ProductName", "Unknown")

            if customer_id not in customer_stats:
                customer_stats[customer_id] = {
                    "total_spent": 0.0,
                    "purchase_count": 0,
                    "products_bought": set()
                }

            customer_stats[customer_id]["total_spent"] += revenue
            customer_stats[customer_id]["purchase_count"] += 1
            customer_stats[customer_id]["products_bought"].add(product)
        except (ValueError, TypeError):
            continue

    # Step 2: Calculate average order value and convert products_bought to list
    for customer, stats in customer_stats.items():
        if stats["purchase_count"] > 0:
            stats["avg_order_value"] = round(
                stats["total_spent"] / stats["purchase_count"], 2
            )
        else:
            stats["avg_order_value"] = 0.0
        stats["products_bought"] = list(stats["products_bought"])

    # Step 3: Sort by total_spent descending
    sorted_customers = dict(
        sorted(customer_stats.items(), key=lambda x: x[1]["total_spent"], reverse=True)
    )

    return sorted_customers

def daily_sales_trend(transactions):
    """
    Analyzes sales trends by date.

    Returns: dictionary sorted by date

    Expected Output Format:
    {
        '2024-12-01': {
            'revenue': 125000.0,
            'transaction_count': 8,
            'unique_customers': 6
        },
        '2024-12-02': {...},
        ...
    }
    """
    daily_stats = {}

    # Step 1: Aggregate stats per date
    for t in transactions:
        try:
            date = t.get("Date", "Unknown")
            qty = int(t.get("Quantity", 0))
            price = float(t.get("UnitPrice", 0.0))
            revenue = qty * price
            customer_id = t.get("CustomerID", "Unknown")

            if date not in daily_stats:
                daily_stats[date] = {
                    "revenue": 0.0,
                    "transaction_count": 0,
                    "unique_customers": set()
                }

            daily_stats[date]["revenue"] += revenue
            daily_stats[date]["transaction_count"] += 1
            daily_stats[date]["unique_customers"].add(customer_id)
        except (ValueError, TypeError):
            continue

    # Step 2: Convert unique_customers set to count
    for date, stats in daily_stats.items():
        stats["unique_customers"] = len(stats["unique_customers"])

    # Step 3: Sort chronologically by date
    sorted_daily_stats = dict(sorted(daily_stats.items(), key=lambda x: x[0]))

    return sorted_daily_stats
