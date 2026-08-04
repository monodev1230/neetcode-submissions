class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums)

        n = len(nums)
        dpWithFirst = [0] * (n)
        dpWithoutFirst = [0] * (n)

        dpWithFirst[0] = nums[0]
        dpWithFirst[1] = max(nums[0], nums[1])
        for i in range(2, n-1):
            dpWithFirst[i] = max(dpWithFirst[i-1], nums[i] + dpWithFirst[i-2])

        dpWithoutFirst[0] = nums[1]
        dpWithoutFirst[1] = max(nums[1], nums[2])
        for i in range(2, n-1):
            dpWithoutFirst[i] = max(dpWithoutFirst[i-1], nums[i+1] + dpWithoutFirst[i-2])

        return max(dpWithFirst[-2], dpWithoutFirst[-2])