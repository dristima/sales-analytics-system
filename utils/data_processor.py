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

    Requirements:
    - Aggregate by ProductName
    - Calculate total quantity sold
    - Calculate total revenue for each product
    - Sort by TotalQuantity descending
    - Return top n products
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

    return top_products