from app.services.APIClient import APIClient
from random import randint
import time

if __name__ == "__main__":
    api = APIClient()

    for i in range(10):
        api.get_user_data(i)
        api.post_config(
            {
                "time"  : time.time(),
                "data"  : randint(0, 1000)
            }
        )
        api.check_health()