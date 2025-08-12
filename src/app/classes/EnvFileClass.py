from dotenv import load_dotenv

from app.classes.FileClass import FileClass


class EnvFileClass(FileClass):
    def read_file(self, path: str) -> any:
        try:
            with open(path, "r", encoding="utf-8") as file:
                return load_dotenv(path)
        except FileNotFoundError as e:
            print(e)
    
    def write_file(self, path: str, data: dict) -> None:
        try:
            with open(path, "w", encoding="utf-8") as file:
                file.write(data)
        except FileNotFoundError as e:
            print(e)