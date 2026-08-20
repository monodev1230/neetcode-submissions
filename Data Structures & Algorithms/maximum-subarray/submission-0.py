class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        res = max(nums)
        for right in range(len(nums)):
            currSum += nums[right]
            if currSum < 0:
                currSum = 0 
            else:
                res = max(res, currSum)
            
        return res