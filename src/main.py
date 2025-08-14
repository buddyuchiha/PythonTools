from app.utils.logging import logger
from app.services.PortScanner import PortScanner
from core.config import config

if __name__ == "__main__":
    ps = PortScanner(
        config['SETTINGS']['HOST'], 
        config['SETTINGS']['PORTS'],
        config['SETTINGS']['THREADS']       
        )
    
    logger.info(
        f"Created PortScanner with adress: {config['SETTINGS']['HOST']}, "
        f"ports: {config['SETTINGS']['PORTS']}, "
        f"threads: {config['SETTINGS']['THREADS']}"
        )
    
    ps.start() 