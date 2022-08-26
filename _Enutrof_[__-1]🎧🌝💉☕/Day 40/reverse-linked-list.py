class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        next_ = None
        while curr:
            prev = next_
            next_ = curr
            curr = curr.next
            next_.next = prev
        return next_
            
