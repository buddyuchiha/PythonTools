from multiprocessing import Process, Queue

from app.utils.logging import logger 
from core.config import config

class FileAnalysis:
    def __init__(self, *args) -> None:
        self.paths = []
        for arg in args:
            self.paths.append(arg)
        
        self.queue = Queue()

    def __analyzer(self):
        while True:

            file_path = self.queue.get()
            with open(file_path, "r", encoding="utf-8") as file:
                

    def __init_processes(self) -> None:
        processes = []
        for path in self.paths:
            self.queue.put(path)

        for i in range(config["SETTINGS"]["PROCESSES_NUM"]):
            p = Process(target=self.__analyzer)
            processes.append(p)

    def start(self) -> None:
        self.__init_processes()