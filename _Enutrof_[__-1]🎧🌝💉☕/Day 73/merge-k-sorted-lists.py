class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        if list1.val > list2.val:
            list1, list2 = list2, list1
            
        home = list1
        
        while list1 is not None and list2 is not None:
            if list2.val >= list1.val:
                try:
                    if list1.next.val < list2.val:
                        list1 = list1.next
                        continue
                except:
                    ...
                stash= (list1.next, list2.next, list2)
                list1.next = list2
                list2.next = stash[0]
                list1, list2, last = stash
            else:
                list1 = last
        else:
            list1 = last
            
        if list2 is not None:
            list1.next = list2
        return home    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        while len(lists) > 1:
            if len(lists) % 2 == 0:
                lists = [self.mergeTwoLists(lists[i], lists[i+1]) for i in range(0, len(lists), 2)]
            else:
                lists = [self.mergeTwoLists(lists[i], lists[i+1]) for i in range(0, len(lists)-1, 2)] + [lists[-1]]
        return lists[0]
