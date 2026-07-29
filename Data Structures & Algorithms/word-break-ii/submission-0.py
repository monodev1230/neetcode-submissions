class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordMap = Counter(wordDict)
        res = []
        cur = []
        def dfs(i):
            if i == len(s):
                res.append(' '.join(cur))
                return
            for j in range(i, len(s)):
                if s[i:j+1] in wordMap:
                    cur.append(s[i:j+1])
                    dfs(j+1)
                    cur.pop()
        dfs(0)
        return res

