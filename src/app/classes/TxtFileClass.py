from app.classes.FileClass import FileClass

class TxtFileClass(FileClass):
    def read_file(self, path: str) -> str:
        try:
            with open(path, "r", encoding="utf-8") as file:
                return file.read() 
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File not found path: {path}") from e

    def write_file(self, path: str, data: str) -> None:
        try:
            with open(path, "w", encoding="utf-8") as file:
                file.write(data)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File not found path: {path}") from e
