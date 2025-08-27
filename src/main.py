import argparse

from app.services.LogsValidater import LogsValidater
from core.config import config


def main():
    lv = LogsValidater()
    
    parser = argparse.ArgumentParser(description='LogsValidater')

    parser.add_argument('-v', '--validate', help='Logs validation')
    parser.add_argument('-a', '--analyze', help='Logs analyze')
    parser.add_argument('-t', '--test', help='Default tests')

    args = parser.parse_args()

    if args.validate:   
        print('Валидацмя логов')
        path = args.validate 
        lv.validate(path)

    if args.analyze:
        print('Анализ логов')
        path = args.analyze
        lv.analyze(path)

    if args.test:
        print("Базовый тест всех функций")

        lv.validate(config['PATH']['BASIC_LOGS'])
        lv.analyze(config['PATH']['ANALYSIS_LOGS'])
        
        print("-"*30)
        print("Продвинутый тест всех функций")
        
        lv.validate(config['PATH']['EDGE_CASES_LOGS'])
        lv.analyze(config['PATH']['EDGE_CASES_LOGS'])


if __name__ == "__main__":
    main()