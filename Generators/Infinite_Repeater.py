from typing import Generator, Any

def infinite_repeater(sequence : list[Any]) -> Generator[Any, None, None]:
    while True:
        for item in sequence:
            yield item

def main() -> None:
    repeater_gen : Generator[Any, None, None] = infinite_repeater([1, 2, 4, 19])

    for _ in range(10):
        print(next(repeater_gen))

if __name__ == '__main__':
    main()