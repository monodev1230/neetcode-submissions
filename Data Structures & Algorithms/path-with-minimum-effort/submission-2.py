from heapq import *
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        minHeap = [[0, 0, 0]]
        visit = set()
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        while minHeap:
            diff, r, c  = heappop(minHeap)
            if (r, c) in visit:
                continue
            visit.add((r, c))

            if (r, c) == (ROWS-1, COLS-1):
                return diff
            
            for dr, dc in dirs:
                newR, newC = dr + r, dc + c
                if not 0 <= newR < ROWS or not 0 <= newC < COLS or (newR, newC) in visit:
                    continue
                newDiff = max(diff, abs(heights[newR][newC] - heights[r][c]))
                heappush(minHeap, [newDiff, newR, newC])
        return 0



            



                



            