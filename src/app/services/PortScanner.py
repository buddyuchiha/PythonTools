from queue import Queue
import re
import socket
import threading
import time

from app.utils.logging import logger
from core.config import config

class PortScanner:
    def __init__(self, adress: str, ports: str, threads_num: int = 5) -> None:
        self.__input_checker(adress, ports, threads_num)

        self.adress = adress
        self.start_port, self.final_port = \
            [int(port) for port in ports.rsplit('-')]

        if self.final_port < self.start_port:
            raise ValueError(f"{self.final_port} < {self.final_port}")

        self.threads_num = threads_num
        self.port_queue = Queue()

    def __input_checker(
        self, 
        adress: str, 
        ports: str, 
        threads_num: int
        ) -> None | Exception:
        if not isinstance(adress, str) \
            or not isinstance(ports, str) \
                or not isinstance(threads_num, int):
                    raise TypeError(
                        f"Wrong types: adress {type(adress)}, "
                        f"ports: {type(ports)}, " 
                        f"threads_num {type(threads_num)}"
                        )

        if not re.fullmatch(r"^\d{1,6}-\d{1,6}$", ports):
            raise ValueError(f"Incorrect ports were input: {ports}")

    def __scanner(self) -> None:
        while True:
            
            port = self.port_queue.get()
            if port is None:
                self.port_queue.task_done()
                break
            
            try: 
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(config["SETTINGS"]["TIMEOUT"])
                result = sock.connect_ex((self.adress, port))
            except Exception as e:
                logger.error(f"Error scanning port {port} : {e}")

            if result == 0:
                logger.info(f"Port {port} is open.")
            else:
                logger.info(f"Port {port} is closed.")    
            
            sock.close()
            self.port_queue.task_done()             

    def __init_threads(self) -> None:
        threads = []

        for port in range(self.start_port, self.final_port + 1):
            self.port_queue.put(port)

        for _ in range(self.threads_num):
            t = threading.Thread(target=self.__scanner)
            threads.append(t)
            t.start()

        self.port_queue.join()

        for _ in range(self.threads_num):
            self.port_queue.put(None)

        for t in threads:
            t.join()
        
    def start(self) -> None:
        logger.info(
            f"Starting scanning ports for adress {self.adress}, "
            f"ports {self.start_port} - {self.final_port}."
            )
                
        start = time.time()
        self.__init_threads()
        finish = time.time()
        
        result = finish - start
        logger.info(f"Time result: {result} seconds.")