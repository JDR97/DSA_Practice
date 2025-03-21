def sum(a, b):
    mask = 0xffffffff

    while(b & mask) != 0:
        carry = (a&b) << 1
        a = a^b

        b = carry

    return (a & mask) if b > 0 else a


a = -5
b = -12

print(sum(a, b))