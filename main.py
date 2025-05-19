from utils.extract import fetch_products
from utils.transform import process_data
from utils.load import save_to_csv, save_to_google_sheets


def main():
    raw_data = fetch_products(pages=50)
    df = process_data(raw_data)
    save_to_csv(df)
    # Change this line to match your actual JSON key file name
    save_to_google_sheets(df, json_keyfile='project-etl-460308-82133f2ce43f.json(1)')

if __name__ == "__main__":
    main()
