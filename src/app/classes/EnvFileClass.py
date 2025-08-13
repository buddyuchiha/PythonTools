from dotenv import dotenv_values

from app.classes.FileClass import FileClass


class EnvFileClass(FileClass):
    def read_file(self, path: str) -> any:
        try:
            with open(path, "r", encoding="utf-8") as file:
                return dotenv_values(stream=file)  
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File not found path: {path}") from e
    
    def write_file(self, path: str, data: dict) -> None:
        try:
            with open(path, "w", encoding="utf-8") as file:
                data = "".join(data)
                file.write(data)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File not found path: {path}") from e
