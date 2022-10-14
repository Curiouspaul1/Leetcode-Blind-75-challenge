# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur=root
        while cur:
            if p.val > root.val and q.val > root.val:
                cur=cur.right
            elif p.val<root.val and q.val <root.val:
                cur=cur.left
            else:
                return cur
            
            
            
        