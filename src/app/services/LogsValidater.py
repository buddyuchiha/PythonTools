import re 

from core.config import config


class LogsValidater:    
    def __init__(self) -> None:
        self.template = config['TEMPLATES']['LOG_TEMPLATE']
    
    def __report_validate(
        self,
        correct_num: int,
        incorrect_num: int, 
        incorrect_list: list[list]
        ) -> None:
        print(
            f"Количество кооректных строк: {correct_num}",
            f"Количество некорректных строк: {incorrect_num}", 
        )

        for data in incorrect_list:
            print(
                f"Номер некорректной строки: {data[0]} \n",
                f"Содержимое: {data[1]}"
            )

    def __validater(self, file_data: str) -> tuple[int, int, list]:
        incorrect_list = []
        line_num = 0

        for line in file_data:
            line_num += 1
            if not re.fullmatch(self.template, line.strip()):
                incorrect_list.append([line_num, line])
        
        incorrect_num = len(incorrect_list)
        correct_num = line_num - incorrect_num

        return correct_num, incorrect_num, incorrect_list

    def validate(self, file_path: str) -> str:     
        try:   
            with open(file_path, "r", encoding='utf-8') as file:
                correct_num, incorrect_num, incorrect_list = \
                    self.__validater(file)

            self.__report_validate(
                correct_num, 
                incorrect_num, 
                incorrect_list
                )
        except FileNotFoundError:
            raise FileNotFoundError(f"Wrong path: {file_path}")

    def __get_statistics(self, data: str) -> list:
        info_list = re.findall(r"\[INFO\]", data)
        warning_list = re.findall(r"\[WARNING\]", data)
        error_list = re.findall(r"\[ERROR\]", data)
        debug_list = re.findall(r"\[DEBUG\]", data)

        statistics = [
            ['INFO', len(info_list)],
            ['WARNING', len(warning_list)],
            ['ERROR', len(error_list)],
            ['DEBUG', len(debug_list)]
        ]

        return statistics

    def __analyzer(self, file_data: str) -> tuple[int, list, list]:
        correct_num = 0
        correct_lines = []

        for line in file_data:
            strip_line = line.strip()

            if re.fullmatch(self.template, strip_line):
                correct_num += 1
                correct_lines.append(line)

        correct_file_data = " ".join(correct_lines)

        timedate_list = re.findall(
            r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}", correct_file_data
            )

        statistics = self.__get_statistics(correct_file_data)

        return correct_num, statistics, timedate_list

    def __report_analyze(
        self,
        correct_num: int, 
        statistics: list, 
        time_range: list   
        ) -> None:

        print(f"Общее количество корректных записей: {correct_num}")
        print("Статиска по уровням логирования")

        for statistic in statistics:
            print(
                f"Уровень логгирования: {statistic[0]} \n", 
                f"Количество записей: {statistic[1]}"
                )

        print(
            f"Самая раняя дата записи: {time_range[0]} \n",
            f"Самая поздняя дата записи: {time_range[1]}"            
            )

    def analyze(self, file_path: str) -> str:
        try: 
            with open(file_path, "r", encoding='utf-8') as file:
                file_data = file.readlines()
                correct_num, statistics, time_range = \
                    self.__analyzer(file_data) 

            self.__report_analyze(
                correct_num,
                statistics, 
                time_range
            )
        except FileNotFoundError:
            raise FileNotFoundError(f"Wrong path: {file_path}")