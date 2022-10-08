# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _isBSTUtil(self, node: Optional[TreeNode], minVal: int, maxVal: int) -> bool:
        if node == None:
            return True
        
        if node.val < minVal or node.val > maxVal:
            return False
        
        return self._isBSTUtil(node.left, minVal, node.val-1) and self._isBSTUtil(node.right, node.val+1, maxVal)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self._isBSTUtil(root, -2**31, 2**31-1)
