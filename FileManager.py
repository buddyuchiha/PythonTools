import os

class FileManager:
    def __init__(self):
        pass
    
    def view_directory(self, path: str) -> list[str]:
        if os.path.exists(path):
            return os.listdir(path) 

    def get_directory(self) -> str:
        return os.getcwd()

    def create_directory(self, path: str) -> None:
        if not os.path.exists(path):
            os.mkdir(path)
             
    def remove_file(self, path: str) -> None:
        if os.path.exists(path):
            os.remove(path)
    
    def remove_dircetory(self, path: str) -> None:
        if os.path.exists(path):
            files = self.view_directory(path)
            if files != []:
                for file in files:
                    file_path = path + '/' + file
                    self.remove_file(file_path)
            os.rmdir(path)
    
    def rename(self, path: str, name: str) -> None:
        if os.path.exists(path) and not os.path.exists(name):
            os.rename(path, name)
    
    def __get_fd(self, path: str) -> int:
        fd = os.open(path, os.O_RDWR | os.O_CREAT ) 
        return fd 
    
    def read_file(self, path: str) -> bytes:  
        fd = self.__get_fd(path)
             
        data = os.read(fd, os.path.getsize(path))
        
        os.close(fd)
        
        return data 
    
    def write_file(self, path: str, data: bytes) -> None:
        fd = self.__get_fd(path)
        
        os.write(fd, data)
        
        os.close(fd)
    
    def copy_file(self, path: str, new_path: str) -> None:   
        if os.path.exists(path):
            data = self.read_file(path)
            
            self.write_file(new_path, data)
  
    def change_directory(self, path: str = None) -> None:
        if os.path.exists(path):
            os.chdir(path)
    
    def get_stat(self, path: str) -> os.stat_result:
        return os.stat(path)