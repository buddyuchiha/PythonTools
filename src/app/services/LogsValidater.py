import re 


class LogsValidater:
    def __init__(self, template: re) -> None:
        self.template = template
    
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

    def __validater(self, file_data: str) -> str:
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
        with open(file_path, "r", encoding='utf-8') as file:
            correct_num, incorrect_num, incorrect_list = self.__validater(file)

            return self.__report_validate(
                correct_num, 
                incorrect_num, 
                incorrect_list
                )