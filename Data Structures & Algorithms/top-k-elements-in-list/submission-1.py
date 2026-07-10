class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        ans = []
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        bucket = [[] for i in range(len(nums) + 1)]
        for key, val in freq.items():
            bucket[val].append(key)
        
        for frequency in range(len(nums), -1, -1):
            for num in bucket[frequency]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        return ans