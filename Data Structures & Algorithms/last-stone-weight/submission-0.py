from heapq import *
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = []
        for stone in stones:
            heappush(minHeap, -stone)

        while len(minHeap) > 1:
            x = -heappop(minHeap)
            y = -heappop(minHeap)
            if x != y:
                heappush(minHeap, -abs(x-y))
            
        return -minHeap[0] if len(minHeap) == 1 else 0
