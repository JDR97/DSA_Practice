def reverseBit(n):
    res = 0

    for _ in range(32):
        bit = n & 1
        res = (res << 1) | bit
        n >>= 1

    return res



n = 43261596
print(reverseBit(n))