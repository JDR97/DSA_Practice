def hasTripletSum(arr, target):
    n = len(arr)
    arr.sort()

    for i in range(n-2):
        j = i+1
        k = n-1

        reqSum = target - arr[i]
        while j < k:
            if arr[j] + arr[k] == reqSum:
                return True
            if arr[j] + arr[k] < reqSum:
                j += 1
            else:
                k -= 1

    return False

#Another approach
def hasTripletSum2(arr, target):
    n = len(arr)
    for i in range(n-2):
        st = set()

        for j in range(i+1,n):
            thirdEle = target - arr[i] - arr[j]
            if thirdEle in st:
                return True
            st.add(arr[j])

    return False


if __name__ == "__main__":
    arr = [1, 4, 45, 6, 10, 8]
    target = 13
    if hasTripletSum(arr, target):
        print("true")
    else:
        print("false")