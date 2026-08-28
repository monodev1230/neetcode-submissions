class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupSet = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            groupSet[key].append(word)

        return list(groupSet.values())