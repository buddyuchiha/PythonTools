from app.classes.TxtFileClass import TxtFileClass
from app.config_manager.ConfigManager import ConfigManager
from core.config import config

if __name__ == "__main__":
    txt_file_class = TxtFileClass()
    config_manager = ConfigManager(
        txt_file_class
    )
    txt_file_class.create_file(config["PATH"]["TXT_FILE_PATH"])
    config_manager.handle(config["PATH"]["TXT_FILE_PATH"])
    config_manager.update_file('12345')
    print(config_manager.read_file())
    config_manager.delete_file()