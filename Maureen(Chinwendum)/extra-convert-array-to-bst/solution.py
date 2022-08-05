# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
 def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        _len = len(nums)
        def helper(list1,start,end):
            if start > end:
                return
            mid = (end-start)//2 # finging the mid in list and separating two lists for left sub_tree and right sub_tree
            root = TreeNode(list1[mid]) # creating a node for the mid element
            root.left = helper(list1[:mid],0,mid-1) # creating a left subtree EX: [  -10 , -3,  ]  0 , 5 , 9  => [-10,-3] left subtree
            root.right = helper(list1[mid+1:],mid+1,len(list1)-1) # creating a right subtree EX: -10 , -3, 0 ,[ 5 , 9 ] => [5,9] right subtree
            #and so on....				
            return root 
        return helper(nums,0,_len)