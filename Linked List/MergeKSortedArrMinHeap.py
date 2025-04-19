import heapq

def mergeK(arr, k):
    res = []

    h = []

    for i in range(len(arr)):
        heapq.heappush(h, (arr[i][0], i, 0));

    while h:
        val, rp, cp = heapq.heappop(h)
        res.append(val)
        if cp+1 < len(arr[rp]):
            heapq.heappush(h, (arr[rp][cp+1], rp, cp+1))

    return res


if __name__ == "__main__":
    arr =[[2, 6, 12 ],
          [ 1, 9 ],
          [23, 34, 90, 2000 ]]
    k = len(arr)
    print(k)
    listF = mergeK(arr, k)
    print(listF)