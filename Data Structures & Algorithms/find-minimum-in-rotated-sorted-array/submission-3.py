class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (r - l) // 2 + l
            nextInd = (m + 1) % len(nums)
            if nums[m] > nums[nextInd]:
                return nums[nextInd]
            elif nums[m] < nums[l]:
                r = m - 1
            else:
                l = m + 1
        return nums[0]