from functools import cache
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        @cache
        def dfs(i, currSum):
            if currSum == target:
                return 1
            if i == len(nums) or currSum > target:
                return 0
            take = dfs(0, currSum + nums[i])
            skip = dfs(i + 1, currSum)
            return take + skip

        
        return dfs(0, 0)
        
