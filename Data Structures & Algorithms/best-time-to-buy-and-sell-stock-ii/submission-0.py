class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            dx = prices[i] - prices[i-1]
            if dx > 0:
                profit += dx
        return profit