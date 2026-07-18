class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = len(nums) + 1
        l, curr_sum = 0, 0
        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum >= target:
                min_len = min(min_len, r-l+1)
                curr_sum -= nums[l]
                l += 1
            
        return min_len if min_len < len(nums) + 1 else 0