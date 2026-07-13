class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            checkPair(nums, i + 1, -nums[i], res)
        return res
    
def checkPair(nums, left, target, res):
    right = len(nums) - 1
    while left < right:
        currSum = nums[left] + nums[right]
        if currSum == target:
            res.append([-target, nums[left], nums[right]])
            right -= 1
            left += 1
            while left < right and nums[left] == nums[left - 1]:
                left += 1
            while left < right and nums[right] == nums[right + 1]:
                right -= 1
        elif currSum > target:
            right -= 1
        else:
            left += 1
        
        
    