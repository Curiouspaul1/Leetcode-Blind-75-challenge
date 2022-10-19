class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        lists = [[1,4,5],[1,3,4],[2,6]]
        
        res = None
        curr_head = None
        
        '''
        
        res = curr_head = None
        for lst in lists:
            curr_head = self.mergeTwoLists(lst, curr_head )
            
        return curr_head
        
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode()
        res = head
        
        # 0 - 1 - 1 -2 -3 -4
       # l1_ponter = 4
      #  l2_pointer = none
        
        while l1 and l2:
            if l1.val < l2.val:
                res.next = l1
                l1 = l1.next
            else:
                res.next = l2
                l2 = l2.next
            
            res = res.next
        
        rem  =  l1 if l1 else l2
        res.next = rem
        
        
        return head.next