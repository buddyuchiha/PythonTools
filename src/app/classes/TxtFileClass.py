from app.classes.FileClass import FileClass

class TxtFileClass(FileClass):
    def __init__(self) -> None:
        super().__init__()

    def read_file(self, path: str) -> str:
        try:
            with open(path, "r", encoding="utf-8") as file:
                return file.read() 
        except FileNotFoundError as e:
            print(e)

    def save_file(self):
        pass 

    def update_file(self, path: str, data: str) -> None:
        try:
            with open(path, "w", encoding="utf-8") as file:
                file.write(data)
        except FileNotFoundError as e:
            print(e) 