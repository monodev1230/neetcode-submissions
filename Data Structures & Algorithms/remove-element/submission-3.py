class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            if nums[i] == val:
                j = i + 1
                while j < len(nums) and nums[j] == val:
                    j += 1
                if j == len(nums):
                    return i
                nums[i], nums[j] = nums[j], nums[i]
        return len(nums)
                

