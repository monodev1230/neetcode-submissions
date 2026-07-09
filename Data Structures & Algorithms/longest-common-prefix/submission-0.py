class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        ans = strs[0]
        for word in strs:
            i = 0
            while i < len(ans) and i < len(word) and ans[i] == word[i]:
                i += 1
            ans = ans[:i]
        return ans
                