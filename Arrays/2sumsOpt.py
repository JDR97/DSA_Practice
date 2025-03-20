def two_sum(arr, target):
    arr.sort()

    j = len(arr)-1
    i = 0

    while(i<j):
        sum = arr[i] + arr[j]
        if sum == target:
            return True
        elif sum < target:
            i += 1
        else:
            j -= 1

    return False


arr = [0, -1, 2, -3, 1]
target = -2

# Call the two_sum function and print the result
if two_sum(arr, target):
    print("true")
else:
    print("false")