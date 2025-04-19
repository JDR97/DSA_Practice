###Brute Force approach
def mergeInterval(intervals):
    res = []
    n = len(intervals)
    ##Sort in case of not sorted
    intervals.sort()

    for i in range(n):
        start, end = intervals[i][0], intervals[i][1]
        ##As that element has already been checked and added based on the condition
        if res and end <= res[-1][1]:
            continue

        ##Add all the element till the overlapping mismatch
        for j in range(i+1, n):
            if intervals[j][0] <= end:
                end = max(intervals[j][1], end)
            else:
                break
        res.append([start, end])

    return res

###Optimized Way
def mergeInterval2(intervals):
    n = len(intervals)
    intervals.sort()

    res = []

    for i in range(n):
        if not res or intervals[i][0] > res[-1][1]:
            res.append(intervals[i])
        else:
            res[-1][1] = max(intervals[i][1], res[-1][1])

    return res        


if __name__ == "__main__":
    intervals =  [[1, 3], [2, 5], [4, 6], [8, 10], [11, 13]]
    
    res = mergeInterval2(intervals)
    for it in res:
        print(it[0], it[1])