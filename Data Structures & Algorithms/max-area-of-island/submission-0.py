class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        ROW, COL = len(grid), len(grid[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(x,y):
            if not 0<=x<ROW or not 0<=y<COL or grid[x][y]==0:
                return 0
            grid[x][y] = 0
            area = 1
            for dx, dy in dirs:
                area += dfs(x+dx, y+dy)
            return area

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r,c))
        return maxArea
            