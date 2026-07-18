class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        freqT = Counter(t)
        minLen = len(s) + 1
        l = 0
        res = ''
        for r in range(len(s)):
            currChar = s[r]
            if currChar in freqT:
                freqT[currChar] -= 1

            while checkFreq(freqT):
                print(freqT)
                if r-l+1 < minLen:
                    res = s[l:r + 1]
                    minLen = r-l+1
                if s[l] in freqT:
                    freqT[s[l]] += 1
                l += 1
        
        return res
            
            
def checkFreq(freqT):
    for k, v in freqT.items():
        if v > 0:
            return False
    return True
        