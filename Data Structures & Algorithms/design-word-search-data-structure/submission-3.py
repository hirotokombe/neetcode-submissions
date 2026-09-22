class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for i in range(len(word)):
            if word[i] == '.':
                for j in curr.children:
                    newWord = word[:i] + j + word[i + 1:]
                    if self.search(newWord):
                        return True
                return False
            elif word[i] not in curr.children:
                return False
            curr = curr.children[word[i]]
        return curr.word
            
