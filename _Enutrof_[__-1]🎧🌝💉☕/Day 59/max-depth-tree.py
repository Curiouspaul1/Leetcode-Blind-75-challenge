class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        pool = deque([root])
        count = 0
        
        while pool:
            l = len(pool)
            count += 1
            for i in range(l):
                node = pool.popleft()
                if node:
                    if node.left:
                        pool.append(node.left)
                    if node.right:
                        pool.append(node.right)
        return count
        
