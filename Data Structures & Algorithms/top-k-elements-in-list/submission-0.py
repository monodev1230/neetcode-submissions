class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = collections.defaultdict(int)
        minHeap = []
        for num in nums:
            freqMap[num] += 1
        for num, freq in freqMap.items():
            heapq.heappush(minHeap, (freq, num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        result = []
        while minHeap:
            freq, num = heapq.heappop(minHeap)
            result.append(num)
        return result