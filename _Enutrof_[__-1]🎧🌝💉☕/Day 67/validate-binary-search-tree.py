class Solution:        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        val = float("-inf")
        stack= deque([])
        while True:
            if root is not None:
                stack.append(root)
                root = root.left
            elif stack:
                root = stack.pop()
                if root.val > val:
                    val = root.val
                else:
                    return False
                root = root.right
            else:
                break
        return True
        
