class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size = len(nums)
        ans = [0] * size * 2
        for i, num in enumerate(nums):
            ans[i] = num
            ans[i+size] = num

        return ans