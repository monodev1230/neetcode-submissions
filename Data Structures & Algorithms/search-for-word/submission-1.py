class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(x, y, i):
            if i == len(word):
                return True
            if 0 > x or x >= len(board) or 0 > y or y >= len(board[0]) or word[i] != board[x][y]:
                return False
            
            temp = board[x][y]
            board[x][y] = '#'
            res = False
            for dx, dy in dirs:
                if dfs(x + dx, y + dy, i+1):
                    res = True
                    break
            board[x][y] = temp
            return res

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True
        return False