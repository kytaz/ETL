from utils.utils_extract import fetch_products
from utils.utils_transform import transform
from utils.utils_load import save_to_csv, save_to_google_sheets

def main():
    raw_data = fetch_products(pages=50)
    df = transform(raw_data)
    print("✅ Data berhasil ditransformasi. Kolom:", df.columns.tolist())
    print("🧾 Contoh data:\n", df.head())
    save_to_csv(df)
    save_to_google_sheets(df, json_keyfile='project-etl-460308-8ae7b5cb6416.json')

if __name__ == "__main__":
    main()
