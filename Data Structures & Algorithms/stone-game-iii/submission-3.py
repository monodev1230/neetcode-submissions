from functools import cache
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [-1] * (n + 1)
        dp[n] = 0

        for i in range(n-1, -1, -1):
            total, best = 0, float('-inf')
            for j in range(i, min(i+3, n)):
                total += stoneValue[j]
                best = max(best, total - dp[j+1])
            dp[i] = best

        if dp[0] == 0:
            return 'Tie'
        return 'Alice' if dp[0] > 0 else 'Bob'