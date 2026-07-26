from heapq import *
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minCapital = []
        maxProfit = []
        currCapital = w
        for i in range(len(profits)):
            heappush(minCapital, (capital[i], profits[i]))
        
        for _ in range(k):
            while minCapital and minCapital[0][0] <= currCapital:
                cap, profit = heappop(minCapital)
                heappush(maxProfit, -profit)
            if not maxProfit:
                break
            currCapital -= heappop(maxProfit)
        
        return currCapital
        



