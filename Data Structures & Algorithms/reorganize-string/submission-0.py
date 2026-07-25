from heapq import *
from collections import deque
class Solution:
    def reorganizeString(self, s: str) -> str:
        freqMap = Counter(s)
        maxHeap = []
        for k, v in freqMap.items():
            heappush(maxHeap, (-v, k))
        prev = None
        res = ''
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            freq, char = heappop(maxHeap)
            freq += 1
            res += char
            if prev:
                heappush(maxHeap, prev)
                prev = None
            if freq != 0:
                prev = (freq, char)

        return res

