class Solution:
    def rob(self, nums: List[int]) -> int:
        maxProfit = 0
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            twoBefore = dp[i-2] if i > 1 else 0
            # threeBefore = dp[i-3] if i > 2 else 0
            dp[i] = max(dp[i-1], nums[i] + twoBefore)
        return dp[n-1]
