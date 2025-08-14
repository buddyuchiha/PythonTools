import logging

from core.config import config

logger = logging.getLogger("PortScanner logger")
formatter = logging.Formatter("%(levelname)s-%(asctime)s-%(message)s")

file_handler = logging.FileHandler(config['PATH']['LOG_FILE'], mode="w")
file_handler.setLevel("INFO")
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setLevel("ERROR")
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)