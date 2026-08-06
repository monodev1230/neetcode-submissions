class Solution:
    def numSquares(self, n: int) -> int:
        i = 1
        nums = []
        while i * i <= n:
            nums.append(i*i)
            i += 1
        dp = [n] * (n + 1)
        dp[0] = 0
        for target in range(1, n + 1):
            for num in nums:
                if num > target:
                    break
                dp[target] = min(dp[target], 1 + dp[target-num])
        return dp[n]