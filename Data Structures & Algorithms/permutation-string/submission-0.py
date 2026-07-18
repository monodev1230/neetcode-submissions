class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqS1 = Counter(s1)
        l = 0
        for r in range(len(s2)):
            if s2[r] in freqS1:
                freqS1[s2[r]] -= 1
            if r - l + 1 > len(s1):
                if s2[l] in freqS1:
                    freqS1[s2[l]] += 1
                l += 1
            contains = True
            print(freqS1)
            for k, v in freqS1.items():
                contains = contains and v == 0
            if contains:
                return True
        return False

        