import logging
from core.config import config


logger = logging.Logger("WebCrawler logger")
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

file_handler = logging.FileHandler(config['PATH']['LOG_FILE'])
file_handler.setLevel("INFO")
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setLevel("ERROR")
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)