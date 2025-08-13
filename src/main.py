import argparse

from app.service.DataMaster import DataMaster


def main():
    dm = DataMaster()

    parser = argparse.ArgumentParser("DataMaster")

    parser.add_argument("--date", type=str, metavar='DATE')
    parser.add_argument(
        "--decimal", 
        nargs=3, 
        metavar=('NUM1', 'operation', 'NUM2')
        )
    parser.add_argument("--uuid", type=int, metavar='VERSION')
    parser.add_argument("--code", nargs=2, metavar=('STRING', 'CODE'))

    args = parser.parse_args()

    if args.date:
        date = args.date
        print(dm.date_handler(date))

    if args.decimal:
        num1, operation, num2 = args.decimal
        print(dm.decimal_handler(num1, operation, num2))

    if args.uuid:
        version = args.uuid
        print(dm.uuid(version))

    if args.code: 
        string, code = args.code
        print(dm.code_string(string, code))


if __name__ == "__main__":
    main()