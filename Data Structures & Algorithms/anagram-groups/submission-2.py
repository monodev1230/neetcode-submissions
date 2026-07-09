class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for word in strs:
            groupName = ''.join(sorted(word))
            if groupName in ans:
                ans[groupName].append(word)
            else:
                ans[groupName] = [word]
        return list(ans.values())