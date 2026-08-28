class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        res = strs[0]
        for word in strs:
            i = len(res)
            while i >= 0 and res != word[:i]:
                i -= 1
                res = res[:i]
        return res
            
