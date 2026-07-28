class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort(reverse=True)
        total = sum(nums)
        if total % k != 0:
            return False
        bucketSize = total // k
        buckets = [0] * k

        def dfs(i):
            if i == len(nums):
                return True
            for bucket in range(k):
                buckets[bucket] += nums[i]
                if buckets[bucket] <= bucketSize and dfs(i+1):
                    return True
                buckets[bucket] -= nums[i]

                if buckets[bucket] == 0: 
                    return False
            return False
        return dfs(0)