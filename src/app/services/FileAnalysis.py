from multiprocessing import Process, Queue, current_process
import re

from app.utils.logging import logger    
from core.config import config

class FileAnalysis:
    def __init__(self, *args) -> None:
        self.paths = []
        for arg in args:
            self.handle_arg(arg)
            self.paths.append(arg)

    @staticmethod
    def handle_lines(data: str) -> int:
        if not isinstance(data, str):
            raise ValueError(f"Path must be string: {type(arg)}")

        lines = re.findall(r"\n", data)

        return len(lines) + 1

    @staticmethod
    def handle_words(data: str) -> int:
        if not isinstance(data, str):
            raise ValueError(f"Path must be string: {type(arg)}")

        words = re.findall(r"\b[\w\d]+\b", data)

        return len(words)
    
    @staticmethod
    def handle_symbols(data: str) -> int:
        if not isinstance(data, str):
            raise ValueError(f"Path must be string: {type(arg)}")

        return len(data)

    @staticmethod
    def analyzer(queue: Queue, result_queue: Queue) -> None:
        while True:
            logger.info(f"Process: {current_process().name}, PID: {current_process().pid}")

            file_path = queue.get()

            if file_path is None:
                queue.put(None)
                break

            with open(file_path, "r", encoding="utf-8") as file:
                data = file.read()
                lines = FileAnalysis.handle_lines(data)
                words = FileAnalysis.handle_words(data)
                symbols = FileAnalysis.handle_symbols(data)
            
            result_queue.put({
                file_path: [lines, words, symbols]
            })

            print(
                f"File with path - {file_path} have {lines} lines, "
                f"{words} words, {symbols} symbols. \n"
            )

    def handle_arg(self, arg: str) -> None:
        if not isinstance(arg, str):
            raise ValueError(f"Path must be string, got {type(arg)}")
        if not arg.endswith(".txt"):
            raise ValueError(f"File must be .txt, got {arg}")

    def handle_queue(self, queue: Queue) -> dict:
        lines = 0
        words = 0
        symbols = 0

        while not queue.empty():
            result = queue.get()
            for value in result.values():
                lines += value[0] 
                words += value[1]
                symbols += value [2]

        return {
            "all_lines:"  : lines,
            "all_words"   : words,
            "all_symbols" : symbols
        }

    def init_processes(self) -> None:
        processes = []
        queue = Queue()
        result_queue = Queue()

        for path in self.paths:
            queue.put(path)

        for _ in range(config["SETTINGS"]["PROCESSES_NUM"]):
            queue.put(None)

        for i in range(config["SETTINGS"]["PROCESSES_NUM"]):
            p = Process(target=FileAnalysis.analyzer, name=f"analyzer-{i}", args=(queue, result_queue))
            processes.append(p)
            p.start()

        for process in processes:
            process.join()

        print(self.handle_queue(result_queue))
            
    def start(self) -> None:
        self.init_processes()