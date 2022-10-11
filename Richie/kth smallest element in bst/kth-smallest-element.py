# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #game plan. in order traversal
        #min heapo
        heeeeeep = []
        heapq.heapify(heeeeeep)
        self.add_to_our_heap(root, heeeeeep)
        
        for i in range(k-1):
            heapq.heappop(heeeeeep)
        
        return heapq.heappop(heeeeeep)
        
    def add_to_our_heap(self, root, heeeeeep):
        if root:
            heapq.heappush(heeeeeep, root.val)
        if root.left:
            self.add_to_our_heap(root.left, heeeeeep)
        if root.right:
            self.add_to_our_heap(root.right, heeeeeep)
