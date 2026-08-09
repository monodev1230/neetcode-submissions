class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        threshold = sum(piles) // 2
        dp = {}
        def dfs(l, r):
            if (l, r) in dp:
                return dp[(l, r)]
            if l > r:
                return 0 
            aliceTurn = (r - l + 1)%2 == 0
            left = piles[l] if aliceTurn else 0
            right = piles[r] if aliceTurn else 0 
            dp[(l, r)] = max(left + dfs(l+1, r), right + dfs(l, r-1))
            return dp[(l, r)]
        return True if dfs(0, n-1) > threshold else False
