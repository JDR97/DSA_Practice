from typing import Generator

def cumulative_sum() -> Generator[float, float, None]:
    total : float = 0
    while True:
        ##This yield runs two times for each call
        new_val : float = yield total
        total += new_val 
        ##Or do, total += yield total
        

def main() -> None:
    cumulative_gen : Generator[float, float, None] = cumulative_sum()
    next(cumulative_gen)

    while True:
        value : float = float(input("Enter the value:"))
        #Sending the value/yielding the value back
        curr_sum : float = cumulative_gen.send(value)
        print(f'Cumulative Sum: {curr_sum}')


if __name__ == '__main__':
    main()