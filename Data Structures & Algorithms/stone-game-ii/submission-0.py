from functools import cache
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)
        aliceTotal = [0]
        @cache
        def dfs(i, M, isA):
            if i >= len(piles):
                return 0 
            res = 0 if isA else float('inf')
            currTotal = 0
            for X in range(1, 2*M+1):
                if X + i - 1 >= N:
                    break
                currTotal += piles[X + i - 1]
                if isA:
                    res = max(res, currTotal + dfs(i + X, max(M, X), False))
                else:
                    res = min(res, dfs(i + X, max(M, X), True))
            return res
        return dfs(0, 1, True)
