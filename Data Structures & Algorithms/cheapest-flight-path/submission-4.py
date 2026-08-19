from heapq import *
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        dist = [[float('inf')] * (k + 5) for _ in range(n)]
        graph = defaultdict(list)
        for s, d, p in flights:
            graph[s].append((d, p))
        minheap = [(0, -1, src)]
        stops = 0

        dist[src][0] = 0
        while minheap:
            price, count, airport = heappop(minheap)
            if airport == dst:
                return price
            if count == k or dist[airport][count + 1] < price:
                continue
            
            for d, p in graph[airport]:
                nextPrice = price + p
                nextCount = count + 1
                if dist[d][nextCount + 1] > nextPrice:
                    dist[d][nextCount + 1] = nextPrice
                    heappush(minheap,(nextPrice, nextCount, d))
            
        return -1

            