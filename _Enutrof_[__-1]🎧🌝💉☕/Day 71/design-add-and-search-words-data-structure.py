class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        
class WordDictionary:

    def __init__(self):
        self.dictionary = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.dictionary
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

    def search(self, word: str) -> bool:
        return self.matchWildcard(word, self.dictionary)
        
    def matchWildcard(self, word, dictionary):
        curr = dictionary
        for i, c in enumerate(word):
            if c in curr.children:
                curr = curr.children[c]
            elif c == '.':
                for child in curr.children.values():
                    if self.matchWildcard(word[i+1:], child): 
                        return True
                return False
            else:
                return False
        return curr.isWord
