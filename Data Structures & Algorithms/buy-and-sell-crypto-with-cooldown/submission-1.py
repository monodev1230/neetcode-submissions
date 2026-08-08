from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        dp[(len(prices), True)] = 0
        dp[(len(prices), False)] = 0
        dp[(len(prices) + 1, True)] = 0
        dp[(len(prices) + 1, False)] = 0

        def dfs(i, canBuy):
            if (i, canBuy) in dp:
                return dp[(i, canBuy)]
            res = dfs(i+1, canBuy)
            if canBuy:
                buy = -prices[i] + dfs(i+1, False)
                res = max(buy, res)
            else:
                sell = prices[i] + dfs(i+2, True)
                res = max(sell, res)
            dp[(i, canBuy)] = res
            return res
            
        return dfs(0, True)
            
            
            
            