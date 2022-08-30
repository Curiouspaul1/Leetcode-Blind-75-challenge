class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy= ListNode()
        tail = dummy
        (l1, l2) = (list1, list2)
        
        while l1 and l2:
            if l1.val< l2.val:
                tail.next = l1
                l1= l1.next
            else:
                tail.next= l2
                l2 = l2.next
            tail= tail.next
            
        if l1:
            tail.next = l1
        elif l2:
            tail.next= l2
            
        return dummy.next
