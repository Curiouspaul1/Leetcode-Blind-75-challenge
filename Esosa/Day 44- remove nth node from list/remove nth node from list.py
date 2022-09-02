class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        left = dummy
        right = head
            
        while n> 0 and right:
            right= right.next
            n-=1

        while right:
            left= left.next
            right= right.next
        #delete
        left.next= left.next.next
        return dummy.next
