from heapq import *
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        visited = set()
        heap = [(0, 0)]

        total = 0

        while len(visited) < n:
            cost, i = heappop(heap)

            if i in visited:
                continue

            visited.add(i)
            total += cost

            x1, y1 = points[i]

            for j in range(n):
                if j in visited:
                    continue

                x2, y2 = points[j]

                distance = abs(x1 - x2) + abs(y1 - y2)

                heappush(heap, (distance, j))

        return total