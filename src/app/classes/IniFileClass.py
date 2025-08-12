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
            print(e)
    
    def write_file(self, path: str, data: dict) -> None:
        try:
            with open(path, "w", encoding="utf-8") as file:
                self.config.write(path, data)
        except FileNotFoundError as e:
            print(e)