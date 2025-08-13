from app.classes import (
    TxtFileClass,
    JsonFileClass,
    CsvFileClass,
    YamlFileClass,
    IniFileClass,
    EnvFileClass
)

class ConfigManager:
    def __init__(self) -> None:
        self.txt_file_object = TxtFileClass()
        self.json_file_object = JsonFileClass()
        self.csv_file_object = CsvFileClass()
        self.yaml_file_object = YamlFileClass()
        self.ini_file_object = IniFileClass()
        self.env_file_object = EnvFileClass()


    def handle_path(self, path: str) -> None:
        self.path = path
        match path:
            case _ if path.endswith(".txt"):
                self._file_work = self.txt_file_object
            case _ if path.endswith(".json"):
                self._file_work = self.json_file_object
            case _ if path.endswith(".csv"):
                self._file_work = self.csv_file_object 
            case _ if path.endswith(".yaml"):
                self._file_work = self.yaml_file_object    
            case _ if path.endswith(".env"):
                self._file_work = self.env_file_object   

    def read_file(self, path: str = None) -> any:
        if path:
            self.handle_path(path)

        return self._file_work.read_file(self.path) 

    def write_file(self, data: str, path: str = None) -> None:
        if path:
            self.handle_path(path)
            
        self._file_work.write_file(self.path, data) 

    def delete_file(self, path: str = None) -> None:
        if path: 
            self.handle_path(path)
            
        self._file_work.delete_file(self.path) 

    def repath(self, path: str, new_type: str) -> str:
        new_path = ''

        for i in path:
            if i == '.':
                break
            new_path += i 
        
        return new_path + new_type

    def convert_file(self, input_path: str, new_type: str) -> None:
        data = self.read_file(input_path)

        new_path = self.repath(input_path, new_type)

        self.write_file(data, new_path)
