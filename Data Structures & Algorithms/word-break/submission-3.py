class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = {len(s): True}
        
        def dfs(i):
            if i in dp:
                return dp[i]

            for j in range(i, len(s)):
                if s[i:j+1] in wordSet and dfs(j+1):
                    dp[i] = True
                    return True
            dp[i] = False
            return False
        return dfs(0)
                    
        