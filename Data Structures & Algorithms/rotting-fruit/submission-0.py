from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        freshCnt = 0
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        ROWS, COLS = len(grid), len(grid[0])
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    freshCnt += 1
        time = 0
        while q and freshCnt > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    newR, newC = r + dr, c + dc
                    if 0 <= newR < ROWS and 0 <= newC < COLS and grid[newR][newC] == 1:
                        q.append((newR, newC))
                        grid[newR][newC] = 2
                        freshCnt -= 1
            
            time += 1
        
        return time if freshCnt == 0 else -1