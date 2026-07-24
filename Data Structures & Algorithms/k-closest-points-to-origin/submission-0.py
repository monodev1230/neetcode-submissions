from heapq import *
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        res = []
        for point in points:
            distance = math.sqrt(point[0]*point[0] + point[1]*point[1])
            heappush(maxHeap, (-distance, point))
            if len(maxHeap) > k:
                heappop(maxHeap)
        for _, point in maxHeap:
            res.append(point)
        return res