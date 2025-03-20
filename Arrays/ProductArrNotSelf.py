def productArr(arr):
    n = len(arr)
    ans = [1]*n

    for i in range(1, n):
        ans[i] = ans[i-1] * arr[i-1]
    
    right = 1
    for i in range(n-1, -1, -1):
        ans[i] *= right
        right *= arr[i]

    return ans



arr = [-1,1,0,-3,3]
output = productArr(arr)
print(output)