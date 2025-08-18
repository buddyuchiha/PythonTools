from app.services.FileAnalysis import FileAnalysis
from core.config import config


if __name__ == "__main__":
    fa = FileAnalysis(
        config['PATH']['TEST_FILE_1'], 
        config['PATH']['TEST_FILE_2'],
        config['PATH']['TEST_FILE_3']
        )

    fa.start()