class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start, end = 0, len(nums) - 1
        i = 0
        while i < len(nums):
            print("start", start, 'end', end, 'i', i, 'nums[i]',nums[i])
            if nums[i] == 0:
                nums[start], nums[i] = nums[i], nums[start]
                start += 1
                i += 1
            elif nums[i] == 2 and i < end:
                nums[end], nums[i] = nums[i], nums[end]
                end -= 1
            else:
                i += 1
        return nums


        