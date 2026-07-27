class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        freqMap = Counter(nums)

        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for num in freqMap:
                if freqMap[num] > 0:
                    curr.append(num)
                    freqMap[num] -= 1
                    dfs(curr)
                    curr.pop()
                    freqMap[num] += 1
        dfs([])
        return res