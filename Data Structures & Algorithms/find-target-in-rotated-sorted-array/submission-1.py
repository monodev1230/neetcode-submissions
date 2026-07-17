class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1 2 3 4 5 6 -1 0 
        # 5 6 -1 0 1 2 3 4
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (r - l) // 2 + l
            if nums[m] == target:
                return m
            # left sorted
            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            #right sorted
            else:
                if target < nums[m] or nums[r] < target:
                    r = m - 1
                else:
                    l = m + 1

        return -1