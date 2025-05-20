import gspread
from gspread_dataframe import set_with_dataframe

# ... fungsi lain ...

def save_to_google_sheets(df, json_keyfile='project-etl-460308-464de4f7c024.json', sheet_url='https://docs.google.com/spreadsheets/d/1Vy4rViij8jDSrV6JoEEz0Whcl-QVN8X3l0_lMlYM85A/edit?usp=sharing'):
    try:
        gc = gspread.service_account(filename=json_keyfile) # <-- Baris ini yang melakukan otentikasi
        sh = gc.open_by_url(sheet_url)
        worksheet = sh.sheet1
        worksheet.clear()
        set_with_dataframe(worksheet, df)
    except Exception as e:
        print(f"[ERROR] Gagal menyimpan ke Google Sheets: {e}")
