void dfs(TreeNode* node, int& count, int target, int& res) {
        if (!node) return;
        dfs(node->left, count, target, res);
        count++;
        if (count == target) {
            res = node->val;
            return;
        }
        dfs(node->right, count, target, res);
    }
    int kthSmallest(TreeNode* root, int k) {
        int count = 0;
        int res;
        dfs(root, count, k, res);
        return res;
    }
