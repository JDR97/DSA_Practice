##Powershell is an issue, try executing it in command prompt
from typing import Generator

def fibonacci_generator() -> Generator[int, None, None]:
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a+b

def main() -> None:
    fib_gen : Generator[int, None, None] = fibonacci_generator()
    n : int = 10
    line_break : str = '-' * 20

    while True:
        input(f'Tap "enter" to generate {n} fibonacci numbers:')
        print(line_break)
        for i in range(n):
            print(next(fib_gen))
        print(line_break)

if __name__ == '__main__':
    main()