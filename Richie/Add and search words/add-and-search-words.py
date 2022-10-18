class TrieNode:
    def __init__(self):
        self.links = {}
        self.end = False
    
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        self.maxL = 0   #store the maximum length of all the words inserted
        
    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        l = 0
        for w in word:
            if w not in node.links:
                node.links[w] = TrieNode()
            node = node.links[w]
            l += 1
        
        self.maxL = max(self.maxL, l)
        node.end = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) > self.maxL:    #optimization
            return False
        
        def helper(index, node):
            for inn in range(index, len(word)):
                c = word[inn]
                if c == ".":
                    for child in node.links.values():
                        if helper(inn+1, child):
                            return True
                    return False
                else:
                    if c not in node.links:
                        return False
                    node = node.links[c]

            return node.end
        return helper(0, self.root)