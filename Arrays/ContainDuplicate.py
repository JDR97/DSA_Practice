def findDup(arr):
    arr.sort()
    n = len(arr)

    for i in range(n):
        if arr[i-1] == arr[i]:
            return arr[i]
        
    return -1


arr = [1, 2, 4, 5, 3, 9, 2]
res = findDup(arr)
print(res)