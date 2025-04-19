#It has multiple approaches,
## 1. Maintaining count of the numbers in an Array
## 2. Maintaining a hash to keep count of the members (1 to N)
## 3. Using Maths formula, sum of N natural numbers and sum of squares of n natural numbers
## 4. Using XOR bitwise operation

from typing import List

def findMissingRepeatingNumbers(arr):
    n = len(arr)

    SN = (n*(n+1))//2
    S2N = (n*(n+1) * (2*n + 1)) // 6

    S, S2 = 0, 0

    for i in range(n):
        S += arr[i]
        S2 += arr[i] * arr[i]

    value1 = S-SN
    value2 = S2 - S2N
    value2 = value2//value1

    x = (value1 + value2)//2
    y = x - value1

    return [x, y]

def findMissingRepeatingNumbers2(arr):
    n = len(arr)
    xr = 0

    for i in range(n):
        xr = xr^arr[i]
        xr = xr^(i+1)

    dif_bit = (xr & ~(xr-1))

    zero_gp = 0
    one_gp = 0
    for i in range(n):
        if(arr[i] & dif_bit == 0):
            zero_gp = zero_gp ^ arr[i]
        else:
            one_gp = one_gp ^ arr[i]

    for i in range(1, n+1):
        if(i & dif_bit != 0):
            one_gp = one_gp ^ i
        else:
            zero_gp = zero_gp ^ i

    count = 0
    for i in range(n):
        if arr[i] == zero_gp:
            count += 1

    if count == 2:
        return [zero_gp, one_gp]
    
    return [one_gp, zero_gp]



if __name__ == '__main__':
    a = [3, 1, 2, 5, 4, 6, 7, 5]
    ans = findMissingRepeatingNumbers2(a)
    print("The repeating and missing numbers are: {", ans[0], ", ", ans[1], "}\n")