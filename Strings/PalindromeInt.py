def palindrome(num):
    revNum = 0
    dup = num

    while(dup):
        lastDigit = dup%10
        revNum = (revNum * 10) + lastDigit
        dup = dup//10

    if revNum == num:
        return True
    else:
        False


def main():
    number = 45540

    if palindrome(number):
        print(number, "is a palindrome.")
    else:
        print(number, "is not a palindrome.")


if __name__ == "__main__":
    main()