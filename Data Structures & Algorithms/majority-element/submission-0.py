class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # [1,2,3,2,1,2,2,3,2,3]
        n = len(nums)
        cand = None
        vote = 0
        for num in nums:
            if num == cand:
                vote += 1
            elif vote == 0:
                cand = num
                vote += 1
            else:
                vote -= 1
        return cand