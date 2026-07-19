class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        freqT = Counter(t)
        minLen = len(s) + 1
        l, matched = 0, 0
        res = ''
        for r in range(len(s)):
            currChar = s[r]
            if currChar not in freqT:
                continue

            freqT[currChar] -= 1
            if freqT[currChar] == 0:
                matched += 1

            while matched == len(freqT):
                if r-l+1 < minLen:
                    res = s[l:r + 1]
                    minLen = r-l+1
                if s[l] in freqT:
                    freqT[s[l]] += 1
                    if freqT[s[l]] > 0:
                        matched -= 1
                l += 1
        
        return res
        #ADOBECODEBANC


