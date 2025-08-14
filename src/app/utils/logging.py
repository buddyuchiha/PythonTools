import logging

from core.config import config


logger = logging.Logger("FileAnalysis logger")
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

file_handler = logging.FileHandler(config['PATH']['LOG_FILE'], 'w', encoding='utf-8')
file_handler.setLevel("INFO")
file_handler.setFormatter(formatter)

logger.addHandler(logger)