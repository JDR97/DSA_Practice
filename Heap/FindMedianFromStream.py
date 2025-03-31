import heapq

class MedianFinder(object):

    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        small, large = self.heaps
        heapq.heappush(small, -heapq.heappushpop(large, num))
        if len(large) < len(small):
            heapq.heappush(large, -heapq.heappop(small))       

    def findMedian(self):
        """
        :rtype: float
        """
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0]-small[0])/2.0