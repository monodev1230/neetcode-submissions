class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(j, node):
            cur = node
            for i in range(j, len(word)):
                ch = word[i]
                if ch == '.':   
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if ch not in cur.children:
                        return False
                    cur = cur.children[ch]
            return cur.word
        return dfs(0, self.root)
