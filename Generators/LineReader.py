import sys
from typing import Generator

def read(path : str) -> Generator[str, None, str]:
    with open(path, 'r') as file:
        for line in file:
            yield line.strip()

    return "The Ending..."

def main() -> None:
    reader : Generator[str, None, str] = read('note.txt')
    input("Press 'enter'--- ")

    while True:
        try:
            print(next(reader))
        except StopIteration as e:
            print("Stop Iteration:", e.value)
            sys.exit()

        input()

if __name__ == '__main__':
    main()