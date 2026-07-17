class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 1 2 3 4 5 6
        # 4 5 6 7 1 2 
        # 5 6 7 1 2 3 4
        # 6 1 2 3 4 5
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (r - l) // 2 + l
            nextInd = (m + 1) % len(nums)
            if nums[m] >= nums[nextInd]:
                return nums[nextInd]
            elif nums[m] < nums[l]:
                r = m - 1
            else:
                l = m + 1
        return -1