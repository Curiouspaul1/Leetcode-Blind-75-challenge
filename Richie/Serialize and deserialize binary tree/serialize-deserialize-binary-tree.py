# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "[]"
        queue=[root]
        res=[str(root.val)]
        while queue:
            node=queue.pop(0)
            if node.left:
                queue.append(node.left)
                res.append(str(node.left.val))
            else:
                res.append('null')
            
            if node.right:
                queue.append(node.right)
                res.append(str(node.right.val))
            else:
                res.append('null')
            
           
            
        return ",".join(res)
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data=="[]":
            return None
        data_list=data.split(",")
        root=TreeNode(int(data_list[0]))
        queue=[root]
        i,start,end=1,1,1
        while end<=len(data):
            end=start+2**i
            j=start
            while j<end and queue:
                
                node=queue.pop(0)
                
                if data_list[j]!='null':
                    node.left=TreeNode(int(data_list[j]))
                else:
                    node.left=None
                
                if data_list[j+1]!='null':
                    node.right=TreeNode(int(data_list[j+1]))
                else:
                    node.right=None
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                j+=2
                
            start=end
                
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
