
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(nums) or (i != len(nums)-1 and nums[i] == 0):
                return False
            if i == len(nums) - 1:
                return True

            for step in range(1,nums[i]+1):
                res = dfs(i + step)
                if i + step not in memo:
                    memo[i+step] = res
                if res:
                    return True
            return False
        
        return dfs(0)