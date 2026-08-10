class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def dfs(cur):
            if cur == n:
                return 1
            if cur > n:
                return 0
            if cur not in dp:
                dp[cur] = dfs(cur+1) + dfs(cur+2)
            return dp[cur]
            
        return dfs(0)
