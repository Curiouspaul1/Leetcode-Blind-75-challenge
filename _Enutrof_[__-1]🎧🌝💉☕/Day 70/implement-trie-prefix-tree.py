class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
class Trie:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.trie
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self.trie
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return curr.isWord
    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        for c in prefix:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return True
