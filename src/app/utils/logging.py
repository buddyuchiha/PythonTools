import logging

from core.config import config

logger = logging.Logger("info logger")
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

file_handler = logging.FileHandler(config["PATH"]["LOGS"], mode="a")
file_handler.setFormatter(formatter)
file_handler.setLevel("INFO")

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel("ERROR")

logger.addHandler(file_handler)
logger.addHandler(stream_handler)