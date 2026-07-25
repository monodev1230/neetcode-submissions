from heapq import *
from collections import deque
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        minEnqTimeHeap = []
        minProcTimeHeap = []
        res = []
        for i, task in enumerate(tasks):
            heappush(minEnqTimeHeap,(task[0], task[1], i))
        readyQ = deque()
        time = 0
        while minEnqTimeHeap or minProcTimeHeap:
            while minEnqTimeHeap and minEnqTimeHeap[0][0] <= time:
                enqTime, procTime, i = heappop(minEnqTimeHeap)
                heappush(minProcTimeHeap, (procTime, i))
            if not minProcTimeHeap:
                time = minEnqTimeHeap[0][0]
                continue
            processTime, index = heappop(minProcTimeHeap)
            time += processTime
            res.append(index)
        return res
