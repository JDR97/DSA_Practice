def hiddenSeq(diff_arr, upper, lower):
    curr = 0
    max_val = 0
    min_val = 0

    for i in diff_arr:
        curr = curr + i
        max_val = max(curr, max_val)
        min_val = min(curr, min_val)

        if((upper-max_val) - (lower-min_val) + 1 <= 0):
            return 0
        
    return ((upper-max_val) - (lower-min_val) + 1)


diff_arr = [1, -3, 4]
upper = 6
lower = 1
print(hiddenSeq(diff_arr, upper, lower))
