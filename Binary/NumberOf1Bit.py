def hammingWeight(a):
    res = 0

    for i in range(32):
        if (a >> i) & 1 :
            res += 1

    return res

a = 11
print(hammingWeight(a))