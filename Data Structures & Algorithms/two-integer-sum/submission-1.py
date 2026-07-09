class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lkp = {}
        for i, num in enumerate(nums):
            if target-num in lkp:
                return [lkp[target-num], i]
            lkp[num] = i
        return [-1, -1]