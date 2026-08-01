class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if len(board) == 0 or len(board[0]) == 0:
            return board

        dirs = [(0,1),(0,-1), (1,0),(-1,0)]
        visited = set()
        ROWS, COLS = len(board), len(board[0])

        def dfs(x, y, cur):
            if not 0 <= x < ROWS or not 0 <= y < COLS or board[x][y] != "O" or (x, y) in visited:
                return 
            isEdge = False
            if x == 0 or x == ROWS - 1 or y == 0 or y == COLS - 1:
                isEdge = True
            cur.append((isEdge, (x, y)))
            visited.add((x,y))
            for dx, dy in dirs:
                dfs(x + dx, y + dy, cur)

        def markSurrounded(region):
            for _, coord in region:
                x, y = coord
                board[x][y] = "X"

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in visited:
                    region = []
                    dfs(r, c, region)
                    isSurrounded = True
                    for isEdge, coord in region:
                        if isEdge:
                            isSurrounded = False
                    if isSurrounded:
                        markSurrounded(region)
                    