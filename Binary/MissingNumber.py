def missingNumber(a , N):
    xor1 = 0
    xor2 = 0

    for i in range(len(a)):
        xor1 ^= a[i]
    for i in range(1, N+1):
        xor2 ^= i

    res = xor1 ^ xor2

    return res


def main():
    N = 5
    a = [1, 2, 4, 5]
    ans = missingNumber(a, N)
    print("The missing number is:", ans)


if __name__ == '__main__':
    main()