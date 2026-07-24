from heapq import *

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        self.cap = k
        for num in nums:
            heappush(self.minHeap, num)
            if len(self.minHeap) > self.cap:
                heappop(self.minHeap)
            
    def add(self, val: int) -> int:
        heappush(self.minHeap, val)
        if len(self.minHeap) > self.cap:
            heappop(self.minHeap)
        return self.minHeap[0]
