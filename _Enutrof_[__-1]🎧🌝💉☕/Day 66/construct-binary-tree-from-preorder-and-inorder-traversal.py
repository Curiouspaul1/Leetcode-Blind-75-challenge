class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            position = inorder.index(preorder.pop(0))
            node = TreeNode(inorder[position])
            node.left = self.buildTree(preorder, inorder[:position])
            node.right = self.buildTree(preorder, inorder[position+1:])
			
            return node
