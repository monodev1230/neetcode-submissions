class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False
        n = len(s)
        dp = [False] * (n + maxJump)
        dp[n-1] = True 

        for i in range(n-2, -1, -1):
            if s[i] == '0':
                for j in range(minJump, maxJump+1):
                    if dp[i + j]:
                        dp[i] = True
                        break
        return dp[0]
                
