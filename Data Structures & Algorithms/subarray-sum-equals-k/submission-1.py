class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0: 1}
        count = 0 
        sum = 0 
        for num in nums:
            sum += num
            if sum-k in prefixSum:
                count += prefixSum[sum-k]
            prefixSum[sum] = prefixSum.get(sum, 0) + 1
        return count