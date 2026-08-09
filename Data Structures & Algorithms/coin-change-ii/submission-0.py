from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        res = [0]
        @cache
        def dfs(i, curr):
            if curr == amount:
                return 1
            if curr > amount or i == len(coins):
                return 0
            return dfs(i, curr + coins[i]) + dfs(i + 1, curr)
        return dfs(0, 0)
