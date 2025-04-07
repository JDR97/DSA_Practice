from typing import Generator
import csv
import sys

def csv_row_reader(file_path : str) -> Generator[list[str], None, None]:
    with open(file_path,'r') as csv_file:
        for row in csv.reader(csv_file):
            yield(row)

def main() -> None:
    csv_gen : Generator[list[str], None, None] = csv_row_reader('data.csv')

    while True:
        try:
            for i in range(3):
                print(next(csv_gen))
            input("Continue to retrive data----")
        except StopIteration:
            print("End of data in the file")
            sys.exit()


if __name__ == '__main__':
    main()