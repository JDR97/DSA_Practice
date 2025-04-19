##There are two approach one with sorting starting value(Greedy)
#second is sorting ending values 

def minRemovalStart(intervals):
    count = 0
    intervals.sort(key=lambda x : x[0])

    end = intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] < end:
            count += 1
            end = min(end, intervals[i][1])
        else:
            end = intervals[i][1]

    return count


def minRemovalEnd(intervals):
    count = 0

    intervals.sort(key= lambda x : x[1])

    end = intervals[0][1]

    for i in range(1, len(intervals)):
        #As the end is already sorted in ASC, we do not need to assign again
        if intervals[i][0] < end:
            count += 1
        else:
            end = intervals[i][1]

    return count
        


if __name__ == "__main__":
    intervals = [[1, 2], [2, 3], [3, 5], [1, 4]]
    print(minRemovalEnd(intervals))