# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def dfs(root):
            if not root:
                return 0
            leftMax = dfs(root.right)
            rightMax = dfs(root.left)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            
            res[0] = max(res[0], root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax) 
        dfs(root)
        return res[0]
