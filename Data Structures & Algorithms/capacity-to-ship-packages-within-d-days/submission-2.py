class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        res = right
        while left <= right:
            mid = (right - left) // 2 + left
            cDays, currWeight = 0, 0
            for weight in weights:
                currWeight += weight
                if currWeight > mid:
                    cDays += 1
                    currWeight = weight        
            cDays += 1

            if cDays <= days:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1

        return res