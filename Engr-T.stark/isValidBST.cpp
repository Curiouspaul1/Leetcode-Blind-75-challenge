class Solution {
public:
    vector<int> list = {};
    
    vector<int> traverseInOrder(TreeNode* node, vector<int> &l) {
        if(node == NULL) return {};
        traverseInOrder(node->left, l);
        l.push_back(node->val);
        traverseInOrder(node->right, l);
        return l;
    }
    
//     bool isSorted(vector<int> l) {
//         if(l.size() < 1) return true;
        
//         for(int i = 0; i < l.size()-1; i++) {
//             if(l[i] > l[i + 1]) return false;
//         }
//         return true;
//     }
    
    bool isValidBST(TreeNode* root) {
        vector<int> l = traverseInOrder(root, list);
        
        for(int i = 0; i < l.size()-1; i++) 
        {
            if(l[i] >= l[i + 1]) return false;
        }
        return true;
    }
};
