class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        levels = []
        
        while queue:
            levels.append([])
            for _ in range(len(queue)):
                node = queue.popleft()
                levels[-1].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return levels
