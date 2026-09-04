class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        res = []
        visit = set()
        dirs = [[0,1], [1, 0], [0, -1], [-1, 0]]
        def dfs(r, c, dir):
            if not 0 <= r < ROWS or not 0 <= c < COLS or (r, c) in visit:
                return False
            res.append(matrix[r][c])
            visit.add((r, c))
            newR = r + dirs[dir][0]
            newC = c + dirs[dir][1]
            if not dfs(newR, newC, dir):
                dir = (dir + 1) % 4
                dfs(r + dirs[dir][0], c + dirs[dir][1], dir)
            return True
        dfs(0, 0, 0)
        return res

