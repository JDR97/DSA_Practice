from collections import Counter
import heapq

def topKFrequent(arr, k):
    n = len(arr)

    mp = Counter(arr)
    freq = list(mp.items())
    freq.sort(key=lambda x : (x[1], x[0]), reverse=True)
    res = []
    print(freq)
    for i in range(k):
        res.append(freq[i][0])

    return res

#Using priority queue/heap, there are other two approaches also check GFG
def topKFrequent2(arr, k):
    mp = Counter(arr)
    pq = []

    for key, value in mp.items():
        heapq.heappush(pq, (value, key))
        if len(pq) > k:
            heapq.heappop(pq)

    res = []

    while pq:
        res.append(heapq.heappop(pq)[1])

    res.reverse()
    return res


if __name__ == "__main__":
    arr = [3, 1, 4, 4, 5, 2, 6, 1]
    k = 2
    res = topKFrequent2(arr, k)
    
    for val in res:
        print(val, end=" ")