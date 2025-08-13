import json 

from app.classes.FileClass import FileClass

class JsonFileClass(FileClass):
    def read_file(self, path: str) -> dict:
        try:
            with open(path, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File not found path: {path}") from e
    
    def write_file(self, path: str, data: dict) -> None:
        try:
            with open(path, "w", encoding="utf-8") as file:
                json.dump(data, file)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File not found path: {path}") from e
