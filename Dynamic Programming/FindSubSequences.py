def findSubSequences(curr, arr, subArr, res):
    n = len(arr)

    if curr == n:
        res.append(subArr.copy())
        return
    
    subArr.append(arr[curr])

    findSubSequences(curr+1, arr, subArr, res)
    subArr.pop()
    findSubSequences(curr+1, arr, subArr, res)


if __name__ == "__main__":
    arr = [1,2,3]

    subArr = []
    res = []

    findSubSequences(0, arr, subArr, res)

    for subSeq in res:
        print(" ".join(map(str, subSeq)))