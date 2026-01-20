def parse_transactions(raw_lines):
    """
    Parses raw sales data lines into a list of transaction dictionaries.

    Each line is expected to be pipe-delimited with fields:
    TransactionID|Date|ProductID|ProductName|Quantity|UnitPrice|CustomerID|Region

    Returns: list of dictionaries with keys:
    ['TransactionID', 'Date', 'ProductID', 'ProductName',
     'Quantity', 'UnitPrice', 'CustomerID', 'Region']
    """

    transactions = []

    for line in raw_lines:
        parts = line.strip().split("|")

        # Skip malformed rows
        if len(parts) < 8:
            continue

        # Clean product name (remove commas if present)
        product_name = parts[3].replace(",", "")

        # Convert numeric fields safely
        try:
            quantity = int(parts[4].replace(",", "")) if parts[4] else 0
        except ValueError:
            quantity = 0

        try:
            unit_price = float(parts[5].replace(",", "")) if parts[5] else 0.0
        except ValueError:
            unit_price = 0.0

        transaction = {
            "TransactionID": parts[0],
            "Date": parts[1],
            "ProductID": parts[2],
            "ProductName": product_name,
            "Quantity": quantity,
            "UnitPrice": unit_price,
            "CustomerID": parts[6],
            "Region": parts[7]
        }

        transactions.append(transaction)

    return transactions   # <-- CRUCIAL