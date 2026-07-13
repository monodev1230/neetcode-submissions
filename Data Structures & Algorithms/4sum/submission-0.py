class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quads = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                twoSum(nums, nums[i], nums[j], j + 1, target, quads)
        return quads
                
def twoSum(nums, first, second, left, target, quads):
    right = len(nums) - 1
    while left < right:
        currSum = first + second + nums[left] + nums[right]
        if currSum == target:
            quads.append([first, second, nums[left], nums[right]])
            left += 1
            right -= 1
            while left < right and nums[left] == nums[left-1]:
                left += 1
            while left < right and nums[right] == nums[right+1]:
                right -= 1
        elif currSum > target:
            right -= 1
        else:
            left += 1