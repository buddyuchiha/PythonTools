from app.utils.logging import logger
from app.services.PortScanner import PortScanner
from core.config import config

if __name__ == "__main__":
    ps = PortScanner(
        config['SETTINGS']['HOST'], 
        config['SETTINGS']['PORTS']        
    )

    logger.info(
        f"{ps.adress}"
        f"ports: {ps.start_port} - {ps.final_port}, "
        f"threads: {ps.threads_num}"
        )
    
    ps.start() 