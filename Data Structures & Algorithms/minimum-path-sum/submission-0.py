class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[float('inf')] * (n+1) for _ in range(m+1)]
        dp[m-1][n] = 0
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                dp[r][c] = min(dp[r+1][c], dp[r][c+1]) + grid[r][c]
        return dp[0][0]