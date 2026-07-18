class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        lkp = {}
        for r in range(len(nums)):
            if nums[r] in lkp:
                return True
            else:
                lkp[nums[r]] = 1
            
            if r >= k:
                del lkp[nums[l]]
                l += 1
        return False
            