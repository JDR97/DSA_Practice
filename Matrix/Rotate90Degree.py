#Transpose of the matrix and reverse each row
def rotate(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    for i in range(n):
        arr[i].reverse()

#Create a new matrix and move element there
def rotate2(arr):
    n = len(arr)
    rotated = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n-i-1] = arr[i][j]

    return rotated

if __name__ == "__main__":
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    #rotate(arr)
    rot = rotate2(arr)
    print("Rotated Image")
    for i in range(len(rot)):
        for j in range(len(rot[0])):
            print(rot[i][j], end=" ")
        print()