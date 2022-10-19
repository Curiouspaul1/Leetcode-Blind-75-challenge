class TrieNode:
    def __init__(self):
        self.children={}
        self.endOf=False
class WordDictionary:
    def __init__(self):
        self.root=TrieNode()
        
    def addWord(self, word: str) -> None:
        curr=self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
            curr=curr.children[c]
        curr.endOf=True
    def search(self, word: str) -> bool:
        def dfs(i, node):
            for c in range(i, len(word)):
                if word[c]==".":
                    for k in node.children.values():
                       if dfs(c+1, k):
                            return True
                    return False
                else:
                    if word[c] not in node.children:
                        return False
                    node=node.children[word[c]]
            return node.endOf
        return dfs(0,self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)