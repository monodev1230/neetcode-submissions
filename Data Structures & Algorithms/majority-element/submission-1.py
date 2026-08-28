class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        memo = defaultdict(int)
        for num in nums:
            memo[num] += 1
        major = (-1, 0)
        for k, v in memo.items():
            if v > major[1]:
                major = (k, v)
        return major[0]