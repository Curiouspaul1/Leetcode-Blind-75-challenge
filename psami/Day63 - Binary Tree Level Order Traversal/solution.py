# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode = left
        self.right: TreeNode = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        output_list = []
        output_list.append([])
        output_list[0].append(root.val)


        def dfs(root: TreeNode, no):
            if not root:
                return
            try:
                x= output_list[no]
            except IndexError:
                output_list.append([])

            output_list[no].append(root.val)
            dfs(root.left, no+1)
            dfs(root.right, no+1)
        dfs(root.left, 1)
        dfs(root.right, 1)

        return output_list

        
