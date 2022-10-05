# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q=[root]
        res=[[root.val]]
        while q:
            lis=[]
            num=len(q)
            for i in range(num):
                curr=q.pop(0)
                if curr.left:
                    lis.append(curr.left.val)
                    q.append(curr.left)
                if curr.right:
                    lis.append(curr.right.val)
                    q.append(curr.right)
            if len(lis) != 0:
                res.append(lis)
        return res
                
        