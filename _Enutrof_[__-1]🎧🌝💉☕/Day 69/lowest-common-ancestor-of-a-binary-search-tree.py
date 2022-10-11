class Solution:    
    def getAncestry(self, root: 'TreeNode', node: 'TreeNode', ancestors):
        ancestors.append(root)
        if node.val > root.val:
            self.getAncestry(root.right, node, ancestors)
        elif node.val < root.val:
            self.getAncestry(root.left, node, ancestors)
        else:
            return
            
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if not (q.val <= root.val <= p.val):
        #     return root
        self.p_ancestors = deque([])
        self.q_ancestors = deque([])
        
        self.getAncestry(root, p, self.p_ancestors)
        self.getAncestry(root, q, self.q_ancestors)
        while self.q_ancestors:
            curr = self.q_ancestors.pop()
            if curr in self.p_ancestors:
                return curr
            
