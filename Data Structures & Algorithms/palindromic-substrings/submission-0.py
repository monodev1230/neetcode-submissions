class Solution:
    def countSubstrings(self, s: str) -> int:
        res = [0]
        def checkPalindrome(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res[0] += 1
                left -= 1
                right += 1
        
        for i in range(len(s)):
            checkPalindrome(i, i)
            if i < len(s) - 1:
                checkPalindrome(i, i+1)
                
        return res[0]