from abc import ABC, abstractmethod
import os 


class FileClass(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def read_file(self):
        pass 

    def create_file(self, path: str = None) -> None:        
        with open(path, "w", encoding="utf-8"):
            pass 

    @abstractmethod
    def write_file(self):
        pass

    def delete_file(self, path: str) -> None:
        os.remove(path)

    def convert_file(self):
        pass 