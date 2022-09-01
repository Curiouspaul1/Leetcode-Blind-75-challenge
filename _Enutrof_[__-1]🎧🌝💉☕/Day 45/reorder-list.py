class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        queue = deque()
        while head:
            curr = head
            head = head.next
            curr.next = None
            queue.append(curr)
        print(queue)
        
        curr = queue.popleft()
        end = True
        
        while queue:
            next_ = queue.pop() if end else queue.popleft()
            end = False if end else True
            
            curr.next = next_
            curr = curr.next
            
