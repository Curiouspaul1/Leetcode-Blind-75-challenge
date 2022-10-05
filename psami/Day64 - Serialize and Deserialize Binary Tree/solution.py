# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        if not root:
            return ""
        output_list = []

        output_list.append(str(root.val))


        def dfs(root: TreeNode):
            if not root:
                output_list.append('null')
                return
            output_list.append(str(root.val))

            dfs(root.left)
            dfs(root.right)   
        dfs(root.left)
        dfs(root.right)


        return "#".join(output_list)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        input_list = data.split("#")
        
        self.i = 0

        def pop():
            if input_list[self.i] == "null":
                self.i += 1
                return None
            head = TreeNode(input_list[self.i])
            self.i +=1
            head.left =pop()
            head.right =pop()
            return head



       
        return pop()

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))