class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        res = 0
        def countNeighbors(x,y):
            neighs = 0
            for dx,dy in dirs: 
                if 0 <= dx + x < len(grid) and 0 <= dy + y < len(grid[0]) and grid[dx+x][dy+y]:
                    neighs += 1
            return neighs
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    res += 4
                    neighs = countNeighbors(r,c)
                    res -= neighs
        return res

