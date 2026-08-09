from functools import cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        t = len(s3)
        if n + m != t or abs(n-m) > 1:
            return False
        @cache
        def dfs(i, j, k):
            if k == t:
                return i == n and j == m

            if i < n and s1[i] == s3[k]:
                if dfs(i + 1, j, k + 1):
                    return True
            if j < m and s2[j] == s3[k]:
                if dfs(i, j + 1, k + 1):
                    return True
            return False

        return dfs(0, 0, 0)