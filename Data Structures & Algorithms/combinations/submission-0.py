class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(i, curr):
            if len(curr) == k:
                res.append(curr.copy())
                return
            if i > n:
                return
            curr.append(i)
            print(i, curr)
            dfs(i + 1, curr)
            curr.pop()
            dfs(i + 1, curr)

        dfs(1, [])
        return res
            