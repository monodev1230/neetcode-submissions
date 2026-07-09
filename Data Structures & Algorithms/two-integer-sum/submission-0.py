class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lkp = {}
        for idx, num in enumerate(nums):
            if target-num in lkp:
                return [lkp[target-num], idx]
            lkp[num] = idx

        return [-1, -1]