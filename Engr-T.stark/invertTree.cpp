class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (root == NULL) return root;
        
//         swap(root->right, root->left);
//         invertTree(root->left);
//         invertTree(root->right);
        
//         return root;
        queue<TreeNode*> q;
        q.push(root);
        
        while(!q.empty())
        {
            TreeNode* t = q.front();
            q.pop();
            swap(t->right, t->left);
            if(t->right) q.push(t->right);
            if(t->left) q.push(t->left);
        }
        return root;
    }
};
