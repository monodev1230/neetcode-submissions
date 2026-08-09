
# class Solution:
#     def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
#         m = len(matrix)
#         n = len(matrix[0])
#         dirs = [(0,1), (0,-1), (1, 0), (-1, 0)]
#         dp = {}

#         def dfs(x, y, prev):
#             if not 0<=x<m or not 0<=y<n or matrix[x][y] <= prev:
#                 return 0
#             if (x,y) in dp:
#                 return dp[(x,y)]
#             res = 1
#             for dx, dy in dirs:
#                 newX, newY = dx + x, dy + y
#                 res = max(res, 1+dfs(newX, newY, matrix[x][y]))
#             dp[(x,y)] = res
#             return res
#         res = 0
#         for x in range(m):
#             for y in range(n):
#                 dfs(x, y, float('-inf'))
#         return max(dp.values())

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}  # (r, c) -> LIP

        def dfs(r, c, prevVal):
            if (r < 0 or r == ROWS or c < 0 or
                c == COLS or matrix[r][c] <= prevVal
            ):
                return 0
            if (r, c) in dp:
                return dp[(r, c)]

            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            dp[(r, c)] = res
            return res

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
        return max(dp.values())
