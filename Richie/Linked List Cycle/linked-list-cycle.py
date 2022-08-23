class Solution:
    def hasCycle(self, head):
        try:
            fast = head.next.next
            slow = head.next
            while head.next:       
                if fast == slow:
                    return True

                slow = slow.next
                fast = fast.next.next
            return False
        except:
            return False
