import csv

from app.classes.FileClass import FileClass


class CsvFileClass(FileClass):
    def read_file(self, path: str) -> list:
        try:
            with open(path, "r", newline='', encoding="utf-8") as file:
                reader = csv.reader(file)
                
                data = []
                for row in reader:
                    data.append(row)

                return data
        except FileNotFoundError as e:
            print(e)
            
    def write_file(self, path: str, data: list[list]) -> None:
        try:
            with open(path, "w", newline='', encoding="utf=8") as file:
                writer = csv.writer(file)
                writer.writerows(data)
        except FileNotFoundError as e:
            print(e)