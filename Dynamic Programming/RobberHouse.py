def solve(arr):
    n = len(arr)
    prev = arr[0]
    prev2 = 0

    for i in range(1, n):
        pick = arr[i]

        if i > 1:
            pick += prev2
        not_pick = 0 + prev

        cur_i = max(pick, not_pick)
        prev2 = prev
        prev =cur_i

    return prev


def robAmount(arr):
    arr1 = []
    arr2 = []
    n = len(arr)
    for i in range(n):
        if i!=0:
            arr1.append(arr[i])
        if i!=n-1:
            arr2.append(arr[i])
    
    res1 = solve(arr1)
    res2 = solve(arr2)

    return max(res1, res2)


#Circular Array
arr = [2, 3, 2, 6]
print(robAmount(arr))