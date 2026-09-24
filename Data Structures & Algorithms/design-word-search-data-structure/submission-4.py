class TrieNode:

    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(node, idx):
            cur = node
            for nxt in range(idx, len(word)):
                char = word[nxt]
                if char == '.':
                    for child in cur.children.values():
                        if dfs(child, nxt + 1):
                            return True
                if char not in cur.children:
                    return False
                cur = cur.children[char]
            return cur.endOfWord
        return dfs(self.root, 0)