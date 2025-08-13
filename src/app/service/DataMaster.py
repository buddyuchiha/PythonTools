from datetime import datetime
from decimal import Decimal
import uuid
from pytz import timezone as pytz_timezone


from app.utils.logging import logger


class DataMaster:
    def __week_handler(self, date: datetime) -> str:
        try:
            week = datetime.weekday(date)
            match week:
                case 0:
                    return "Monday"
                case 1:
                    return "Tuesday"
                case 2:
                    return "Wednesday"
                case 3:
                    return "Thursday"
                case 4:
                    return "Friday"
                case 5:
                    return "Saturday"
                case 6:
                    return "Sunday"
        except ValueError as e:
            raise ValueError(f"Wrong week for date: {date}") from e

    def __date_difference_handler(self, date: datetime) -> int:
        try:
            actual = datetime.now()
            return date.day - actual.day 
        except ValueError as e:
            raise ValueError(f"Wrong num of days for date: {date}") from e

    def __convert_date_utc(self, date: datetime) -> str:
        try:
            samara_tz = pytz_timezone('Europe/Samara')
            dt = samara_tz.localize(date)
            return dt.timetz().tzinfo
        except ValueError as e:
            raise ValueError(f"Wrong date {date}") from e
        
    def __decimal_checker(
            self, 
            num1: float, 
            operation: str, 
            num2: float
            ) -> None | Exception:
        if not isinstance(num1, (int, float)) \
            and not isinstance(operation, (str)) \
                and not isinstance(num2, (int, float)):
            raise TypeError(f"Wrong type: {num1} {operation} {num2}")

    def decimal_handler(self, num1: float, operation: str, num2: float) -> dict:
        try:
            self.__decimal_checker(num1, operation, num2)

            dec_num1 = Decimal(num1)
            dec_num2 = Decimal(num2)

            num1 = float(num1)
            num2 = float(num2)

            match operation:
                case "/":
                    return {
                        "Decimal" : dec_num1 / dec_num2,
                        "Float"   : num1 / num2
                    }
                
                case "+":
                    return {
                        "Decimal" : dec_num1 + dec_num2,
                        "Float"   : num1 + num2
                    }
                
                case "-":
                    return {
                        "Decimal" : dec_num1 - dec_num2,
                        "Float"   : num1 - num2
                    } 
                
                case "*":
                    return {
                        "Decimal" : dec_num1 * dec_num2,
                        "Float"   : num1 * num2
                    }
        except ValueError as e:
            raise ValueError(f"Wrong operation: {num1} {operation} {num2}") from e


    def date_handler(self, date: str) -> dict:
        if not isinstance(date, str):
            raise TypeError(f"Date must be string {date}") from e
        
        date = datetime.strptime(date, "%d.%m.%Y %H:%M")

        week = self.__week_handler(date)
        difference = self.__date_difference_handler(date)
        samara_utc = self.__convert_date_utc(date)

        return {
            "Week"            : week,
            "Days difference" : difference,
            "Samara UTC"      : samara_utc
        }
    
    def uuid(self, version: int) -> uuid:
        if not isinstance(version, int):
            raise TypeError(f"Wrong type: {version}")
        try:
            match version:
                case 1:
                    return uuid.uuid1().int
                case 2:
                    return uuid.uuid2().int
                case 3:
                    return uuid.uuid3().int
                case 4:
                    return uuid.uuid4().int
        except ValueError as e:
            raise ValueError(f"Wrong value: {version}")
            
    def code_string(self, string: str, code: str) -> bytes:
        if not isinstance(string, str) and not isinstance(code, str):
            raise TypeError(f"Wrong type {string}, {code}")
        
        try:
            match code:
                case "UTF-8":
                    return string.encode("UTF-8")
                case "CP1251":
                    return string.encode("CP1251")
                case "Base64":
                    return string.encode("Base64")
        except ValueError as e:
            raise ValueError(f"Wrong code: {code}")
        
