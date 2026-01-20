def validate_and_filter(transactions, region=None, min_amount=None, max_amount=None):
    """
    Validates transactions and applies optional filters
    """

    total_input = len(transactions)
    invalid_count = 0
    valid_transactions = []

    # Step 1: Validation
    for t in transactions:
        required_keys = ["TransactionID", "Date", "ProductID", "ProductName",
                         "Quantity", "UnitPrice", "CustomerID", "Region"]
        if not all(k in t for k in required_keys):
            invalid_count += 1
            continue

        if not (t["TransactionID"].startswith("T") and
                t["ProductID"].startswith("P") and
                t["CustomerID"].startswith("C")):
            invalid_count += 1
            continue

        if t["Quantity"] <= 0 or t["UnitPrice"] <= 0:
            invalid_count += 1
            continue

        valid_transactions.append(t)

    # Step 2: Print available regions
    regions = sorted(set(t["Region"] for t in valid_transactions))
    print(f"Available regions: {', '.join(regions)}")

    # Step 3: Print transaction amount range
    amounts = [t["Quantity"] * t["UnitPrice"] for t in valid_transactions]
    if amounts:
        print(f"Transaction amount range: min={min(amounts)}, max={max(amounts)}")

    # Step 4: Apply filters
    filtered_by_region = 0
    filtered_by_amount = 0

    if region:
        before = len(valid_transactions)
        valid_transactions = [t for t in valid_transactions if t["Region"] == region]
        filtered_by_region = before - len(valid_transactions)
        print(f"Records after region filter ({region}): {len(valid_transactions)}")

    if min_amount is not None or max_amount is not None:
        before = len(valid_transactions)

        def amount_ok(t):
            amt = t["Quantity"] * t["UnitPrice"]
            if min_amount is not None and amt < min_amount:
                return False
            if max_amount is not None and amt > max_amount:
                return False
            return True

        valid_transactions = [t for t in valid_transactions if amount_ok(t)]
        filtered_by_amount = before - len(valid_transactions)
        print(f"Records after amount filter: {len(valid_transactions)}")

    # Step 5: Summary
    filter_summary = {
        "total_input": total_input,
        "invalid": invalid_count,
        "filtered_by_region": filtered_by_region,
        "filtered_by_amount": filtered_by_amount,
        "final_count": len(valid_transactions)
    }

    return valid_transactions, invalid_count, filter_summary
