# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        val=[]
        def real(root):
            if not root:
                return
            val.append(root.val)
            real(root.left)
            real(root.right)
        real(root)
        val.sort()
        return val[k-1]