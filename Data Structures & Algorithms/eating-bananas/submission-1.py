import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right
        while left <= right:
            mid = (right - left) // 2 + left
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/mid)
            if hours <= h: 
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        return res
