class Solution:
    def mergeKLists(self, lists):
        """
        lists = [[1,4,5],[1,3,4],[2,6]]
        res = [1,4,5,1,3,4,2,6]
        """
        
        heap = []
        dummy = ListNode()
        curr = dummy
        
        for li in lists:
            while li:
                heap.append(li.val)
                li = li.next
        heapq.heapify(heap)
        
        while heap:
            val = heapq.heappop(heap)
            node = ListNode(val)
            curr.next = node
            curr = curr.next
        return dummy.next
