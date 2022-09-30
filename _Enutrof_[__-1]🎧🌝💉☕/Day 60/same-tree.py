class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
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
      
