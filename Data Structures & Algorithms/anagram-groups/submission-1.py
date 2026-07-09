class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lkp = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord in lkp:
                lkp[sortedWord].append(word)
            else:
                lkp[sortedWord] = [word]
        
        return lkp.values()