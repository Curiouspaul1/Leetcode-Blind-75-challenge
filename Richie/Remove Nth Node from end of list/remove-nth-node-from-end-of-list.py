# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        leader = follower = head
        
        i = 0
        while i < n and leader:
            leader = leader.next
            i += 1
            
        if not leader:
            return head.next
        
        prev = None
        while leader:
            prev = follower
            follower = follower.next
            leader = leader.next
            
            
        prev.next = follower.next
        return head
