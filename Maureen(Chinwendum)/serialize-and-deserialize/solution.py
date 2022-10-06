class Codec:

    def serialize(self, root):
        if not root:
            return ''
        q= collections.deque([root])
        res=[str(root.val)]
        while q:
            len_q=len(q)
            for i in range(len(q)):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                    res.append(str(node.left.val))
                if not node.left:
                    res.append('N')                
                if node.right:
                    q.append(node.right)
                    res.append(str(node.right.val))
                if not node.right:
                    res.append('N')              
        return ','.join(res)

    def deserialize(self, data):
        if not data:
            return []
        ser=data.split(',')
        
        root=TreeNode(ser[0])
        q=collections.deque([root])
        ind=1
        while q:
            len_q=len(q)
            for i in range(len_q):
                node=q.popleft()
                if ser[ind]!='N':
                    node.left=TreeNode(ser[ind])
                    q.append(node.left)
                ind+=1
                if ser[ind]!='N':
                    node.right=TreeNode(ser[ind])
                    q.append(node.right) 
                ind+=1
        return root