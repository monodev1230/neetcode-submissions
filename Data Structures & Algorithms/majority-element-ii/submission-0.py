class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        threshold = n//3
        freq = Counter(nums)
        ans = []
        for k, v in freq.items():
            if v > threshold:
                ans.append(k)
        return ans