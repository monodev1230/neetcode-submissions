class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return helper(s, left + 1, right) or helper(s, left, right - 1)
            left += 1
            right -= 1
        return True

        
def helper(word, left, right):
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True