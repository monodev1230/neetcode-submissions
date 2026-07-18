class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, l = 0, 0
        lkp = {}
        for i, c in enumerate(s):
            while c in lkp:
                del lkp[s[l]]
                l += 1
            lkp[c] = 1
            res = max(res, (i - l + 1))
        return res
