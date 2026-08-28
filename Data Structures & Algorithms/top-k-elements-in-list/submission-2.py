class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = Counter(nums)
        minHeap = []
        for num, freq in freqMap.items():
            heapq.heappush(minHeap, (freq, num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return [num for _, num in minHeap]
