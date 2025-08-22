from app.services.LogsValidater import LogsValidater
from core.config import config


if __name__ == "__main__":
    raw_string = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3} \[\w{1,7}\] \[[a-z_-]+\] .+"
    lv = LogsValidater(raw_string)

    lv.validate(config['PATH']['BASIC_LOGS'])