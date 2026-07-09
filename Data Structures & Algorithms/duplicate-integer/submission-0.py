class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lkp = {}
        for num in nums:
            if num in lkp:
                return True
            lkp[num] = num
        return False