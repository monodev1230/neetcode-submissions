class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lkp = Counter(nums)
        maxLen = 0
        for num in nums:
            localMax = 0
            curr = num
            while curr in lkp:
                curr += 1
                localMax += 1
            maxLen = max(localMax, maxLen)
        return maxLen
