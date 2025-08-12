class ConfigManager:
    def __init__(
        self,
        txt_file_object: object
        ):
        self.txt_file_object = txt_file_object
    
    def handle(self, path: str) -> None:
        self.path = path
        match path:
            case _ if path.endswith(".txt"):
                self.file_work = self.txt_file_object
            
    def read_file(self):
        return self.file_work.read_file(self.path) 

    def save_file(self):
        pass 

    def update_file(self, data: str) -> None:
        self.file_work.update_file(self.path, data) 

    def delete_file(self):
        self.file_work.delete_file(self.path) 

    def conver_file(self):
        pass 