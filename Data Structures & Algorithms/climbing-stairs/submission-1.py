from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0]
        cache = [-1] * n
        def dfs(i):
            if i == n:
                return 1
            if i > n:
                return 0
            if cache[i] == -1:
                cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]
        
        return dfs(0)