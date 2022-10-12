#define N 26

class TrieNode {
    public: 
    TrieNode* childs[N];
    bool isEnd = false;
    TrieNode() {
        for (int i = 0; i < N; i++) {
            childs[i] = NULL;
        }
    }
};

class Trie {
public:
    TrieNode* root;
    Trie() {
        root = new TrieNode();
    }
    
    void insert(string word) {
        TrieNode* node = root;
        int idx = 0;
        for(auto c: word)
        {
            idx = c-'a';
            if(!node->childs[idx])
                node->childs[idx] = new TrieNode();
            node = node->childs[idx];
        }
        node->isEnd = true;
    }
    
    bool search(string word) {
        int idx = 0;
        TrieNode *node = root;
        for(auto c : word) {
            idx = c-'a';
            if(!node->childs[idx])
                return false;
            node = node->childs[idx];
        }
        return node->isEnd;
    }
    
    bool startsWith(string prefix) {
        int idx = 0;
        TrieNode *node = root;
        for(auto c : prefix) {
            idx = c-'a';
            if(!node->childs[idx])
                return false;
            node = node->childs[idx];
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
