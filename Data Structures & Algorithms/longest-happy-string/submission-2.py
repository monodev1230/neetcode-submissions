from heapq import *
from collections import deque
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        if a == 0 and b == 0 and c == 0:
            return ''

        maxHeap = []
        for cnt, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if cnt != 0:
                heappush(maxHeap, (cnt, char))

        prev = None
        res = ''
        while maxHeap:
            cnt, char = heappop(maxHeap)
            cnt += 1
            res += char
            if prev:
                heappush(maxHeap, prev)
                prev = None
            if cnt != 0:
                if len(res) > 1 and res[-1] == res[-2] == char:
                    prev = (cnt, char)
                else:
                    heappush(maxHeap, (cnt, char))
        return res
            
            
            
        