# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        visited = set()
        if not head:
            return False
        curr = head.next
        while curr:
            if curr in visited:
                return True
            visited.append(curr)
            curr = curr.next
        return False
            
        