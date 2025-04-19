#### Find minimum number of rooms required to do all the meetings

###naive approach
def minMeetingRooms(start, end):
    n = len(start)
    res = 1
    room = 1

    for i in range(n):
        room = 1
        for j in range(n):
            if(i != j):
                if start[i] >= start[j] and end[j] > start[i]:
                    room += 1

        res = max(res, room)

    return res 

## Two Pointer approach
def minMeetingRooms2(start, end):
    n = len(start)
    res = 0
    room = 0

    start.sort()
    end.sort()
    i=0
    j=0

    while(i<n):
        if start[i] < end[j]:
            room += 1
            i += 1

        else:
            room -= 1
            j += 1

        res = max(res, room)

    return res

##Hashing (Cumulative Sum)
def minMeetingRooms3(start, end):
    n = len(start)
    res = 0
    room = 0

    maxEnd = end[0]
    for i in range(n):
        maxEnd = max(maxEnd, end[i])

    #Count start from 0th index
    meetArr = [0] * (maxEnd + 2)

    for i in range(n):
        meetArr[start[i]] += 1
        meetArr[end[i]] -= 1

    for i in range(len(meetArr)):
        room += meetArr[i]
        res = max(room, res)

    return res


if __name__ == "__main__":
    start = [2, 9, 6]
    end = [4, 12, 10]
    print(minMeetingRooms2(start, end))