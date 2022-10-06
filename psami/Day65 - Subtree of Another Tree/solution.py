# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
                
        def check(root, sub_root):
            if not root and not sub_root:
                return True
            if not root or not sub_root:
                return False
            if root.val == sub_root.val and check(root.right, sub_root.right) and check(root.left, sub_root.left):
                return True
            return False
        if check(root, subRoot):
            return True
        return (self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot))


        

        


            
        
        

            