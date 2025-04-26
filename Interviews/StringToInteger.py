
def checkInteger(str):
    n = len(str)

    for i in range(n):
        if str[0] == "-":
            continue
        if(str[i].isalpha() or str[i].isnumeric() or str[i] == "."):
            continue
        else:
            print("Not an integer value, contains SC")
            return

    print("It is an Integer")

##Without using in-built functions
def convertToInteger(str):
    if not str:
        raise ValueError("String can not be empty")

    is_fraction = False
    dot_count = 0
    is_negative = False
    integer_part = 0
    fractional_part = 0
    fractional_len = 0

    for ch in str:
        if ch == ".":
            dot_count += 1
            if dot_count > 1:
                raise ValueError("Invalid Float: more than one decimal point.")
            is_fraction = True
        elif ch == "-" and ch == str[0]:
            is_negative = True
        elif '0' <= ch <= '9':
            digit = ord(ch) - ord('0')
            if not is_fraction:
                integer_part = integer_part * 10 + digit
            else:
                fractional_part = fractional_part * 10 + digit
                fractional_len += 1
        else:
            raise ValueError("Invalid character found")
   
    if is_negative:
        print("It is a negative number")

    return integer_part + (fractional_part / 10 ** fractional_len)



if __name__ == "__main__":
    str = "123.42"
    print(convertToInteger(str))