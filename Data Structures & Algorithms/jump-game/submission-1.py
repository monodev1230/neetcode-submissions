from functools import cache
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        @cache
        def dfs(i):
            if i == len(nums) or (i != len(nums)-1 and nums[i] == 0):
                return False
            if i == len(nums) - 1:
                return True

            for step in range(1,nums[i]+1):
                if dfs(i + step):
                    return True
            return False
        
        return dfs(0)