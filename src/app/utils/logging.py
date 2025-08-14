import logging

from core.config import config

logger = logging.Logger("PortScanner logger")
formatter = logging.Formatter("%(levelname)s - %(asctime)s - %(message)s")

file_handler = logging.FileHandler(
    config['PATH']['LOG_FILE'],
    mode="w",
    encoding="utf-8"
    )
file_handler.setFormatter(formatter)
file_handler.setLevel("INFO")

logger.addHandler(file_handler)