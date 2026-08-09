from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i, curr):
            if i == len(nums) and curr == target:
                return 1
            if i == len(nums):
                return 0
            return dfs(i + 1, curr + nums[i]) + dfs(i + 1, curr - nums[i])
        return dfs(0, 0)