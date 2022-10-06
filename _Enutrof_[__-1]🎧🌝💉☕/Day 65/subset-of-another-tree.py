class Solution:
    def preorderTraversal(self, p: Optional[TreeNode]) -> List[int]:
        if root:
            return ((root.val,) +
                    self.preorderTraversal(root.left) +
                    self.preorderTraversal(root.right))
        else:
            return (None,)
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        P = self.preorderTraversal(p)
        Q = self.preorderTraversal(q)
        return P == Q
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.val == subRoot.val:
                if self.isSameTree(node, subRoot):
                    return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False
