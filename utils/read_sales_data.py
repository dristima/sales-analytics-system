def read_sales_data(filename):
    """
    Reads sales data from file handling encoding issues.

    Returns: list of raw lines (strings)

    Expected Output Format:
    ['T001|2024-12-01|P101|Laptop|2|45000|C001|North', ...]

    Requirements:
    - Use 'with' statement
    - Handle different encodings (try 'utf-8', 'latin-1', 'cp1252')
    - Handle FileNotFoundError with appropriate error message
    - Skip the header row
    - Remove empty lines
    """

    encodings_to_try = ["utf-8", "latin-1", "cp1252"]

    for enc in encodings_to_try:
        try:
            with open(filename, "r", encoding=enc) as f:
                lines = f.readlines()
                break  # stop once file is successfully read
        except UnicodeDecodeError:
            continue
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            return []

    else:
        # If all encodings failed
        print(f"Error: Could not decode file '{filename}' with supported encodings.")
        return []

    # Clean lines: strip whitespace, skip empty, skip header
    cleaned_lines = []
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:  # skip empty lines
            continue
        if i == 0 and "TransactionID" in line:  # skip header row
            continue
        cleaned_lines.append(line)

    return cleaned_lines