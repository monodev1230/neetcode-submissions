class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lkp = {}
        for char in s:
            lkp[char] = lkp.get(char, 0) + 1

        for char in t:
            if char not in lkp:
                return False
            else:
                lkp[char] -= 1
                if lkp[char] == 0:
                    del lkp[char]
        return len(lkp) == 0