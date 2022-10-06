# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and subRoot:
            return False
        if not subRoot and root:
            return False
        
        if self.isSameTree(root, subRoot) == True: #both exist or nothing 
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, node1, node2):
        if not node1 and not node2:
            return True
            
        elif (node1 and node2) and (node1.val == node2.val):
            return (self.isSameTree(node1.left, node2.left) and self.isSameTree(node1.right, node2.right))
        
        else:
            return False
