class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        freq = Counter(nums)
        for i in range(1, len(nums)+1):
            if i not in freq:
                return i
        return len(nums) + 1