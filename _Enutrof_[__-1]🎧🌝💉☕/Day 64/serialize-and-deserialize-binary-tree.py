class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
            
        result = f'{root.val} '
        nodes = deque([root])
        while nodes:
            node = nodes.popleft()
            if node:
                nodes.append(node.left)
            
                if node.left:
                    result += f'{node.left.val} '
                else:
                    result += ' '
                nodes.append(node.right)
                if node.right:
                    result += f'{node.right.val} '
                else:
                    result += ' '
                
        
        return result.lstrip()
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(' ')
        root = TreeNode(int(data[0]))
        level = [root]
        
        i = 1
        while level:
            temp = []
            for node in level:
                if not node:
                    continue
                if data[i]:
                    left = TreeNode(int(data[i]))
                    temp.append(left)
                    node.left = left
                else:
                    temp.append(None)
                if data[i+1]:
                    right = TreeNode(int(data[i+1]))
                    temp.append(right)
                    node.right = right
                else:
                    temp.append(None)
                i += 2
            level = temp
        
        return root
