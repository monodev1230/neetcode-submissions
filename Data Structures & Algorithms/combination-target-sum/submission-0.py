class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        res = []

        def dfs(i, t, path):
            if t < 0:
                return 
            if t == 0:
                res.append(path.copy())
                return
            for j in range(i, len(nums)):
                path.append(nums[j])
                dfs(j, t-nums[j], path)
                path.pop()
        dfs(0, target, [])
        return res
    