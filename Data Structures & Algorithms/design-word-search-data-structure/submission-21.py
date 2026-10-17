class TreeNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TreeNode()
            curr = curr.children[char]
        curr.word = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            curr = node
            for j in range(i, len(word)):
                if word[j] == ".":
                    for children in curr.children.values():
                        if dfs(j + 1, children):
                            return True
                    return False
                else:
                    if word[j] not in curr.children:
                        return False
                    curr = curr.children[word[j]]
            return curr.word 
        
        return dfs(0, self.root)
                        
