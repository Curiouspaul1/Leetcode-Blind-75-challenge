class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr= deque(maxlen=n+1)
        value = head
        while value is not None:
            arr.append(value)
            value = value.next

        if head.next is not None:
            if n == 1:
                arr[0].next = None
            elif n == len(arr):
                head = arr[1]
            else:
                arr[0].next = arr[1-n]
        else:
            head = None
        return head
      
