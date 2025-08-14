from app.services.PortScanner import PortScanner
from app.utils.logging import logger

if __name__ == "__main__":
    ps = PortScanner(
        '127.0.0.1', 
        '10-12',
        4       
        )
    logger.info("Created PortScanner")
    ps.start()