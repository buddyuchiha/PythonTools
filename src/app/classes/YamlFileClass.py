import yaml

from app.classes.FileClass import FileClass


class YamlFileClass(FileClass):
    def read_file(self, path: str) -> any:
        try:
            with open(path, "r", encoding="utf-8") as file:
                return yaml.safe_load(file)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File not found path: {path}") from e
    
    def write_file(self, path: str, data: dict) -> None:     
        try:
            with open(path, "w", encoding="utf-8") as file:
                yaml.safe_dump(data, file)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File not found path: {path}") from e
