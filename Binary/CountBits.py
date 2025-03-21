def countBits(a):
    ans = [0] * (a+1)
    for i in range(1, a+1):
        ans[i] = ans[i >> 1] + (i & 1)

    return ans


a = 5
print(countBits(a))