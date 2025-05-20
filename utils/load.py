import pandas as pd
import gspread
from gspread_dataframe import set_with_dataframe

def save_to_csv(df, filename='products.csv'):
    try:
        df.to_csv(filename, index=False)
    except Exception as e:
        print(f"[ERROR] Gagal menyimpan ke CSV: {e}")

def save_to_google_sheets(df, json_keyfile='project-etl-460308-464de4f7c024.json', sheet_url='https://docs.google.com/spreadsheets/d/1D2k3gybmOADPQOeXZfOi_xnLNaLrkA1fErpLVoGteLU/edit?gid=0#gid=0'):
    try:
        gc = gspread.service_account(filename=json_keyfile)
        sh = gc.open_by_url(sheet_url)
        worksheet = sh.sheet1
        worksheet.clear()
        set_with_dataframe(worksheet, df)
    except Exception as e:
        print(f"[ERROR] Gagal menyimpan ke Google Sheets: {e}")
