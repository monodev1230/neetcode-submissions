from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for num in nums:
            heappush(minHeap, num)
            if len(minHeap) > k:
                heappop(minHeap)
        return minHeap[0] if len(minHeap) > 0 else None