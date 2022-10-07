
# TreeNode{val: 4, left: TreeNode{val: 1, left: None, right: None}, right: TreeNode{val: 2, left: None, right: None}}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.issametree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or
        self.isSubtree(root.right, subRoot))
    def issametree(self,root, sub):
        if not root and not sub:
            return True
        if root and sub and root.val == sub.val:
            return self.issametree(root.left, sub.left) and self.issametree(root.right, sub.right)