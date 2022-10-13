class TrieNode{
public:
    TrieNode *child[26];
    bool end = false;
    TrieNode(){
        for(int i = 0; i < 26; i++)
            child[i] = NULL;
    }
};


class WordDictionary {
    TrieNode *root ;
public:
    WordDictionary() {
        root =  new TrieNode();
    }
    
    void addWord(string word) {
        int idx = 0;
        TrieNode * node = root;
        for(char c: word) {
            idx = c -'a';
            if(!node->child[idx])
                node->child[idx] = new TrieNode();
            node = node->child[idx];
        }
        node->end = true;
    }
    
    bool search(string word) {
        TrieNode *node = root;
        return search(word, 0, node);
    }
    bool search(string &word, int idx , TrieNode *node ) {
        if(!node) return 0;
        if(idx == word.size()) return node->end;
        if(word[idx] != '.')
            return search(word, idx+1, node->child[word[idx]-'a']);

        for(int key = 0; key< 26; key++)
            if(search(word, idx+1, node->child[key]))
                return true;
        return false;
    }
};
