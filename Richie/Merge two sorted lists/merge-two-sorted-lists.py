
class Solution:
    def mergeTwoLists(self, list1, list2):
        p1 = list1
        p2 = list2
        pointer = ListNode()
        first = pointer
            
        while (p1 != None) & (p2 != None):
            print(p1.val, p2.val)
            if p1.val <= p2.val:
                pointer.next = p1
                p1 = p1.next
            
            else:
                pointer.next = p2
                p2 = p2.next
            
            pointer = pointer.next
            
        if p1:
            pointer.next = p1
        if p2:
            pointer.next = p2
        return first.next
            
            
