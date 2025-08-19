from app.services.WebCrawler import WebCrawler

from core.config import config

if __name__ == "__main__":
    wb = WebCrawler(
        config['ADRESSES']
    ) 

    wb.start()