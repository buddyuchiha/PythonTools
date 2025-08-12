class ConfigManager:
    def __init__(
        self,
        txt_file_object: object,
        json_file_object: object,
        csv_file_object: object,
        yaml_file_object: object,
        ini_file_object: object,
        env_file_object: object
        ):
        self.txt_file_object = txt_file_object
        self.json_file_object = json_file_object
        self.csv_file_object = csv_file_object
        self.yaml_file_object = yaml_file_object
        self.ini_file_object = ini_file_object
        self.env_file_object = env_file_object


    def handle(self, path: str) -> None:
        self.path = path
        match path:
            case _ if path.endswith(".txt"):
                self.file_work = self.txt_file_object
            case _ if path.endswith(".json"):
                self.file_work = self.json_file_object
            case _ if path.endswith(".csv"):
                self.file_work = self.csv_file_object 
            case _ if path.endswith(".yaml"):
                self.file_work = self.yaml_file_object    
            case _ if path.endswith(".env"):
                self.file_work = self.env_file_object   
            
    def read_file(self, path: str = None):
        if path:
            self.handle(path)

        return self.file_work.read_file(self.path) 

    def save_file(self):
        pass 

    def write_file(self, data: str, path: str = None) -> None:
        if path:
            self.handle(path)
            
        self.file_work.write_file(self.path, data) 

    def delete_file(self, path: str = None):
        if path: 
            self.handle(path)
            
        self.file_work.delete_file(self.path) 

    def convert_file(self):
        pass 