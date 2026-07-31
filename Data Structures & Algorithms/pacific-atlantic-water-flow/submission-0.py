class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        pac, atl = set(), set()
        ROWS, COLS = len(heights), len(heights[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(r, c, visitSet, prevHeight):
            if (not 0 <= r < ROWS or not 0 <= c < COLS or (r, c) in visitSet or heights[r][c] < prevHeight):
                return
            visitSet.add((r, c))
            for dr, dc in dirs:
                dfs(r + dr, c + dc, visitSet, heights[r][c])

        for i in range(ROWS):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, COLS - 1, atl, heights[i][COLS-1])
        for i in range(COLS):
            dfs(0, i, pac, heights[0][i])
            dfs(ROWS-1, i, atl, heights[ROWS-1][i])

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res
            