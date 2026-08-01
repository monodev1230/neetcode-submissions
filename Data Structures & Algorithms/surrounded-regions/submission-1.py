class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if len(board) == 0 or len(board[0]) == 0:
            return board

        dirs = [(0,1),(0,-1), (1,0),(-1,0)]
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            if not 0<=r<ROWS or not 0<=c<COLS or board[r][c] != "O":
                return
            board[r][c] = 'T'
            for dr, dc in dirs:
                capture(r+dr, c+dc)
        
        for i in range(ROWS):
            if board[i][0] == 'O':
                capture(i, 0)
            if board[i][COLS-1] == 'O':
                capture(i, COLS-1)
        
        for i in range(COLS):
            if board[0][i] == 'O':
                capture(0, i)
            if board[ROWS-1][i] == 'O':
                capture(ROWS-1, i)
            
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'

                    