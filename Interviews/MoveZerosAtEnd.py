def moveZeros(arr):
    n = len(arr)
    pos = 0  # Position to place the next non-zero element

    for i in range(n):
        if arr[i] != 0:
            arr[pos], arr[i] = arr[i], arr[pos]
            pos += 1

    return arr

arr = [0, 5, 7, 10, 0, 0, 11]
print("Initial Array: ", arr)
moveZeros(arr)
print("Later Array: ", arr)

