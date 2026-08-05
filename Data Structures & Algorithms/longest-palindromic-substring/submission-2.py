class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        maxLen = [0]
        res = [""]

        def checkPalindrome(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            left+=1
            right-=1
            if right - left + 1 >= maxLen[0]:
                maxLen[0] = right - left + 1
                res[0] = s[left:right + 1]
        
        for i in range(len(s)):
            checkPalindrome(i, i)
            if i < len(s) - 1:
                checkPalindrome(i, i+1)
        return res[0]
