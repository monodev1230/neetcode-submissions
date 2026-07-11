class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        for i in range(len(nums)):
            if i > 0:
                prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(len(nums)-1, -1, -1):
            if i < len(nums) - 1:
                suffix[i] = suffix[i+1] * nums[i+1]
        ans = []
        for i in range(len(nums)):
            ans.append(prefix[i]*suffix[i])
        return ans