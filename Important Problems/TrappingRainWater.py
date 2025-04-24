def maxWater(arr):
    res = 0

    for i in range(1, len(arr)-1):
        left = arr[i]
        for j in range(i):
            left = max(left, arr[j])

        right = arr[i]
        for j in range(i+1, len(arr)):
            right = max(right, arr[j])

        res += (min(left, right) - arr[i])

    return res

##Two Pointer approach
def maxWater1(arr):
    left = 1
    right = len(arr) - 2

    lMax = arr[left - 1]
    rMax = arr[right + 1]
    res = 0

    while left <= right:
        if lMax <= rMax:
            res += max(0, lMax - arr[left])
            lMax = max(lMax, arr[left])
            left += 1
        else:
            res += max(0, rMax - arr[right])
            rMax = max(rMax, arr[right])
            right -= 1

    return res


if __name__ == "__main__":
    arr = [2, 1, 5, 3, 1, 0, 4]
    print(maxWater(arr))