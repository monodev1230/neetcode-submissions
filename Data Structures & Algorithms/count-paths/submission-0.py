class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1]*n for _ in range(m)]
        for r in range(1, m):
            for c in range(1, n):
                grid[r][c] = grid[r-1][c] + grid[r][c-1]
        return grid[m-1][n-1]