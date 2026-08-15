from heapq import *
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append([t, v])
        minHeap = [[0, k]]
        visit = set()
        res = 0

        while minHeap:
            time, node = heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)

            res = time
            for t, v in graph[node]:
                if v not in visit:
                    heappush(minHeap, [time+t, v])
        return res if len(visit) == n else -1
            


