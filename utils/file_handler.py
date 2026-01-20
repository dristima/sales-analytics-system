import csv
import os

def read_sales_data(filepath):
    """
    Load sales data from a pipe-delimited text file.
    Returns a list of raw lines (strings).
    """
    with open(filepath, "r", encoding="utf-8") as f:
        return f.readlines()


def load_sales_data(filepath):
    """
    Load sales data into a list of dictionaries using csv.DictReader.
    Each row is parsed by the pipe '|' delimiter.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"{filepath} not found.")

    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="|")
        return list(reader)


def save_output(filepath, content):
    """
    Save processed results to a file.
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)


def read_sales_data_with_fallback(filename):
    """
    Reads sales data from file, trying multiple encodings.
    Cleans out empty lines and header row if present.
    Returns: list of raw lines (strings).
    """
    encodings_to_try = ["utf-8", "latin-1", "cp1252"]

    lines = []
    for enc in encodings_to_try:
        try:
            with open(filename, "r", encoding=enc) as f:
                lines = f.readlines()
                break
        except UnicodeDecodeError:
            continue
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            return []

    else:
        print(f"Error: Could not decode file '{filename}' with supported encodings.")
        return []

    cleaned_lines = []
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        # Skip header row if present
        if i == 0 and "TransactionID" in line:
            continue
        cleaned_lines.append(line)

    return cleaned_lines
           