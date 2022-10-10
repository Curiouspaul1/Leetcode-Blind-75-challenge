# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        array_em = []

        def check(root):
            if not root:
                return 
            array_em.append(root.val)
            check(root.right)
            check(root.left)
        check(root)

        new_arr = sorted(array_em)
        return new_arr[k-1]
