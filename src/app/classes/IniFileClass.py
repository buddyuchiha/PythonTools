import configparser

from app.classes.FileClass import FileClass


class IniFileClass(FileClass):
    def __init__(self):
        self.config = configparser.ConfigParser()
        super().__init__()
    
    def read_file(self, path: str) -> list[str]:
        try:
            return self.config.read(path)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File not found path: {path}") from e
    
    def write_file(self, path: str, data: dict) -> None:
        try:
            for section, options in data.items():
                self.config[section] = options
            with open(path, 'w', encoding='utf-8') as file:
                self.config.write(file)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File not found path: {path}") from e
