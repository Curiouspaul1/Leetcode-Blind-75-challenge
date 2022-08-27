
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        store = []
        while head:
            if head in store:
                return True
            store.append(head)
            head = head.next
        return False
      
