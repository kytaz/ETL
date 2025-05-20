import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Melakukan transformasi data seperti konversi harga dan pembersihan.
    """
    # Mengonversi harga ke dalam Rupiah
    df['Price'] = df['Price'].replace({'Rp': '', '.': ''}, regex=True).astype(int) * 16000

    # Mengonversi rating menjadi float
    df['Rating'] = df['Rating'].replace({'Invalid Rating': '0', '/5': '', ' ': ''}, regex=True).astype(float)

    # Menghapus data yang tidak valid
    df = df[df['Title'] != 'Unknown Product']
    df = df.drop_duplicates()
    df = df.dropna()

    # Kolom 'Size' dan 'Gender' tidak mengandung teks tambahan
    df['Size'] = df['Size'].replace({'Size: ': ''}, regex=True)
    df['Gender'] = df['Gender'].replace({'Gender: ': ''}, regex=True)

    # Menambahkan kolom timestamp
    df['Timestamp'] = pd.to_datetime('now')

    return df
