from utils.file_handler import load_sales_data, save_output
from utils.data_processor import process_sales_data

def main():
    data = load_sales_data(r"C:\Users\Dristima\Downloads\sales_data.txt")
    result = process_sales_data(data)
    save_output("output/report.txt", result)
    print(result)
    print("Analysis complete! Check output/report.txt")

if __name__ == "__main__":
    main()