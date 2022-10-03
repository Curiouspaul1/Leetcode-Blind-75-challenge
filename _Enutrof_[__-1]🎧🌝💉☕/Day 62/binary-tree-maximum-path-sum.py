class Solution:
    def depthTraversal(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftMax = self.depthTraversal(root.left)
        rightMax = self.depthTraversal(root.right)
        leftMax = max(leftMax, 0)
        rightMax = max(rightMax, 0)
        
        self.res[0] = max(self.res[0], root.val + leftMax + rightMax)
        
        return root.val + max(leftMax, rightMax)
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = [root.val]
        self.depthTraversal(root)
        return self.res[0]
        
