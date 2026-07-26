from heapq import *
class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if self.minHeap and self.minHeap[0] < num:
            heappush(self.maxHeap, -heappop(self.minHeap))
            heappush(self.minHeap, num)
        else:
            heappush(self.maxHeap, -num)

        if len(self.maxHeap) - len(self.minHeap) > 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0])/2
        else:
            return -self.maxHeap[0]
        