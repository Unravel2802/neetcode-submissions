class TreeNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TreeNode()
            cur = cur.children[c]

        cur.end = True 

    def search(self, word: str) -> bool:
        def dfs(idx, node):
            if idx == len(word):
                return node.end
            
            c = word[idx]

            if c == '.':
                for child in node.children.values():
                    if dfs(idx + 1, child):
                        return True

            if c not in node.children:
                return False

            return dfs(idx + 1, node.children[c])
        return dfs(0, self.root)