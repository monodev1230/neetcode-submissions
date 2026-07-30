class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        islands = 0
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        def dfs(x, y):
            if not 0<=x<ROW or not 0<=y<COL or grid[x][y] == '0':
                return

            grid[x][y] = '0'

            for dx,dy in dirs:
                dfs(x+dx, y+dy)

        print('is', islands, ROW, COL)
        for x in range(ROW):
            for y in range(COL):
                if grid[x][y] == '1':
                    dfs(x,y)
                    islands += 1
        return islands

