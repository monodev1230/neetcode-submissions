class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        if not prices:
            return res
        buy = prices[0]
        for price in prices:
            if price < buy:
                buy = price
            res = max(res, (price - buy))
        return res
                

