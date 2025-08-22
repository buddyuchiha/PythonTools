from functools import wraps
import logging
import time

from core.config import config


logger = logging.Logger("function logger")
formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
    )

file_handler = logging.FileHandler(
    config['PATH']['LOG_FILE'], 
    'w', 
    encoding='utf-8'
    )
file_handler.setLevel('DEBUG')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setLevel('INFO')
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

def log_call(level=logging.DEBUG):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs) -> any:
            logger.info(f"Function {func.__name__} started")
            try: 
                start_time = time.time()
                result = func(*args, **kwargs)
                result_time = time.time() - start_time
                
                logger.info(
                    f"Function {func.__name__} finished successfully \
                          in {result_time}s"
                    )
                logger.info(f"Result for {args}, {kwargs}: {result}")

                return result
            
            except Exception as e:
                logger.error(
                    f"Function {func.__name__} raise an exception: {e} \
                        for {args}, {kwargs}"
                    )
                raise

        return wrapper
    return decorator