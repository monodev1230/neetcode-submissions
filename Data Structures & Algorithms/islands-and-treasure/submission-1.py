from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        ROW, COL = len(grid), len(grid[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        q = deque()
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        dist = 0
        while q:
            size = len(q)
            for _ in range(size):
                currR, currC = q.popleft()
                for dr, dc in dirs:
                    newR, newC = dr+currR, dc+currC
                    if 0 <= newR < ROW and 0 <= newC < COL and grid[newR][newC] == inf:
                        grid[newR][newC] = dist + 1
                        q.append((newR, newC))
            dist += 1