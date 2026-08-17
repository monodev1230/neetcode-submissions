from heapq import *
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        res = 0
        minheap = [[0, 0, 0]]
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        while minheap:
            level, r, c = heappop(minheap)
            if (r, c) in visit:
                continue
            visit.add((r, c))
            res = max(res, grid[r][c])
            if (r, c) == (ROWS-1, COLS-1):
                return res

            for dr, dc in dirs:
                newR, newC = dr + r, dc + c
                if (newR, newC) not in visit and 0 <= newR < ROWS and 0 <= newC < COLS:
                    heappush(minheap, (grid[newR][newC], newR, newC))
            
        return res