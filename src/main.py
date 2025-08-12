from app.classes import (
    TxtFileClass,
    JsonFileClass,
    CsvFileClass,
    YamlFileClass,
    IniFileClass,
    EnvFileClass
)
from app.config_manager.ConfigManager import ConfigManager
from core.config import config


if __name__ == "__main__":
    txt_file_class = TxtFileClass()
    json_file_class = JsonFileClass()
    csv_file_class = CsvFileClass()
    yaml_file_class = YamlFileClass()
    ini_file_class = IniFileClass()
    env_file_class = EnvFileClass()

    config_manager = ConfigManager(
        txt_file_class,
        json_file_class,
        csv_file_class,
        yaml_file_class,
        ini_file_class,
        env_file_class
    )

    # TXT FILE TEST
    txt_file_class.create_file(config["PATH"]["TXT_FILE_PATH"])
    config_manager.handle(config["PATH"]["TXT_FILE_PATH"])
    config_manager.write_file('12345')
    print(config_manager.read_file())
    config_manager.delete_file()

    # JSON FILE TEST
    config_manager.handle(config["PATH"]["JSON_FILE_PATH"])
    config_manager.write_file(
        {
            "test" : "test",
            123    : 123,
            "ayo"  : False
        }
    )
    print(config_manager.read_file())
    config_manager.delete_file()

    # CSV FILE CLASS
    config_manager.handle(config["PATH"]["CSV_FILE_PATH"])
    config_manager.write_file([["Hello"],["Hi"],["WASSUUUP"]])
    print(config_manager.read_file())
    config_manager.delete_file()

    # YAML FILE CLASS
    config_manager.handle(config["PATH"]["YAML_FILE_PATH"])
    config_manager.write_file(
        {
            "YAML" : "YAML",
            "TEST" : 25,
            "LIST" : ['PYTHON', 'YAML']
        }
    )
    print(config_manager.read_file())
    config_manager.delete_file()

    # INI FILE CLASS
    config_manager.handle(config["PATH"]["INI_FILE_PATH"])
    config_manager.write_file(
        {
            "ini" : "testini",
            123   : 123
        }
    )
    print(config_manager.read_file())
    config_manager.delete_file()

     # ENV FILE CLASS
    config_manager.handle(config["PATH"]["ENV_FILE_PATH"])
    config_manager.write_file(
        "abcde", "avdg"
    )
    print(config_manager.read_file())
    config_manager.delete_file()

