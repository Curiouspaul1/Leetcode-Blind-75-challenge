int sum=INT_MIN;
	int solve(TreeNode* root){
		if(!root) return 0;
		int l = solve(root->left);
		int r = solve(root->right);
		int stPath = max(root->val,max(root->val+l,root->val+r)); 
		int totPath = max(sum,root->val+l+r);
		sum = max(sum,max(stPath,totPath));
		return stPath;
	}
	int maxPathSum(TreeNode* root) {
		solve(root);
		return sum;
	}
