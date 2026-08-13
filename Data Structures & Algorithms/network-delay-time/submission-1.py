from heapq import *
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((t, v))
        minHeap = []
        visited = set()
        heappush(minHeap, (0, k))

        res = 0
        while minHeap:
            time, node = heappop(minHeap)
            if node in visited:
                continue
            res = time
            visited.add(node)

            for t, v in graph[node]:
                if v in visited:
                    continue
                heappush(minHeap, (t + time, v))
        return -1 if len(visited) != n else res


