class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def checkPalindrome(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        res, cur = [], []

        def dfs(i):
            if i == len(s):
                res.append(cur.copy())
                return
            for j in range(i, len(s)):
                if checkPalindrome(i, j):
                    cur.append(s[i:j+1])
                    dfs(j+1)
                    cur.pop()
        dfs(0)
        return res
        
            