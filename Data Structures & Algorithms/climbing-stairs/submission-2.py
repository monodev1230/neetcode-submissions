from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0]
        cache = [-1] * (n + 1)
        def dfs(rest):
            if rest == 0:
                return 1
            if rest < 0:
                return 0 
            if cache[rest] == -1:
                cache[rest] = dfs(rest-1) + dfs(rest-2)
            return cache[rest]
        
        return dfs(n)