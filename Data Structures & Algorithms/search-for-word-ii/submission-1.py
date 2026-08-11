class TrieNode:
    def __init__(self):
        self.children = {}
        self.wordEnd = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        wordsTrie = TrieNode()
        for word in words:
            cur = wordsTrie
            for ch in word:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()
                cur = cur.children[ch]
            cur.wordEnd = True
        
        visited = set()
        M = len(board)
        N = len(board[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        res = set()
        def dfs(i, j, curNode, curWord):
            if not 0 <= i < M or not 0 <= j < N or (i, j) in visited or board[i][j] not in curNode.children:
                return
            visited.add((i, j))
            curNode = curNode.children[board[i][j]]
            curWord += board[i][j]
            if curNode.wordEnd:
                res.add(curWord)
            for di, dj in dirs:
                dfs(di+i, dj+j, curNode, curWord)
            visited.remove((i, j))
        for r in range(M):
            for c in range(N):
                dfs(r, c, wordsTrie, '')
        return list(res)
            
        