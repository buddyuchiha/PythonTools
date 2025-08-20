import logging

from app.utils.logging import log_call
from random import randint


class APIClient:
    @log_call(level=logging.DEBUG)
    def get_user_data(self, user_id: int) -> dict:
        return {
            "status"  :  200,
            "user_id" :  user_id
        }
    
    @log_call(level=logging.DEBUG)
    def post_config(self, config_data: dict) -> bool:
        if randint(0, 3) == 3:
            raise ConnectionError("Connection timeout")
        
        return True
    
    @log_call(level=logging.DEBUG)
    def check_health(self) -> str:
        return "OK"