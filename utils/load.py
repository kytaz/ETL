import pandas as pd
import gspread
from gspread_dataframe import set_with_dataframe

def save_to_csv(df, filename='products.csv'):
    df.to_csv(filename, index=False)

# Baris ini yang diperbaiki: menambahkan tanda kurung () setelah nama fungsi
def save_to_google_sheets(df, json_keyfile='project-etl-460308-8ae7b5cb6416.json', sheet_url='https://docs.google.com/spreadsheets/d/1D2k3gybmOADPQOeXZfOi_xnLNaLrkA1fErpLVoGteLU/edit?usp=sharing'):
    gc = gspread.service_account(filename=json_keyfile)
    sh = gc.open_by_url(sheet_url)
    worksheet = sh.sheet1
    worksheet.clear()
    set_with_dataframe(worksheet, df)
