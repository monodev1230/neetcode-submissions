from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dfs(i, canBuy):
            if i >= len(prices):
                return 0 
            if canBuy:
                buy = -prices[i] + dfs(i+1, False)
                rest = dfs(i+1, True)
                return max(buy, rest)
            else:
                sell = prices[i] + dfs(i+2, True)
                hold = dfs(i+1, False)
                return max(sell, hold)
        return dfs(0, True)
            
            
            
            