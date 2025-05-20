import logging
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def setup_logging():
    """
    Mengatur konfigurasi logging untuk menampilkan informasi
    proses scraping ke konsol.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    return logging.getLogger(__name__)

def fetch_product_data(total_pages: int = 50) -> pd.DataFrame:
    logger = setup_logging()
    site_root = "https://fashion-studio.dicoding.dev"
    headers = {"User-Agent": "Mozilla/5.0"}
    records = []

    try:
        # Iterasi setiap halaman
        for page_num in range(1, total_pages + 1):
            page_url = site_root if page_num == 1 else f"{site_root}/page{page_num}"
            logger.info(f"Mengakses: {page_url}")

            try:
                # Mengirim permintaan HTTP ke halaman
                res = requests.get(page_url, headers=headers, timeout=10)
                res.raise_for_status()

                # Parsing HTML dengan BeautifulSoup
                html_doc = BeautifulSoup(res.text, "html.parser")
                items = html_doc.select(".collection-card")

                # Ekstraksi data dari setiap elemen produk
                for item in items:
                    record = extract_info(item)
                    records.append(record)

            except requests.exceptions.RequestException as e:
                logger.error(f"Request error pada halaman {page_num}: {e}")

        if not records:
            logger.error("Tidak ada data yang berhasil dikumpulkan.")
            return pd.DataFrame()

        return pd.DataFrame(records)
    
    except Exception as e:
        logger.error(f"Error dalam fetch_product_data: {e}")
        return pd.DataFrame()


def extract_info(card) -> dict:
    """
    Ekstrak data dari card produk.
    """
    try:
        def get_text(element, default=""):
            return element.get_text(strip=True) if element else default

        data = {
            "Title": get_text(card.find(class_="product-title"), "Unknown Product"),
            "Price": get_text(card.find(class_="price"), "N/A"),
            "Rating": None,
            "Colors": None,   
            "Size": None,     
            "Gender": None,   
            "Timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')  
        }

        descs = card.find_all("p")
        for desc in descs:
            text = desc.get_text(strip=True)
            if text.startswith("Rating:"):
                data["Rating"] = text.replace("Rating:", "").strip()
            elif "Colors" in text:
                data["Colors"] = text.replace("Colors", "").strip()
            elif text.startswith("Size:"):
                data["Size"] = text.replace("Size:", "").strip()
            elif text.startswith("Gender:"):
                data["Gender"] = text.replace("Gender:", "").strip()

        return data

    except Exception as e:
        logger.error(f"Error dalam extract_info: {e}")
        return {
            "Title": "Error",
            "Price": "N/A",
            "Rating": None,
            "Colors": None,
            "Size": None,
            "Gender": None,
            "Timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
