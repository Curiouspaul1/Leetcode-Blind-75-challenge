class Solution:
    def reverseList(self, head):
        prevN = None
        currN = head
        
     
        while head != None:
            nextN = currN.next
            currN.next = prevN
            prevN = currN
            currN = nextN

            if nextN == None:
                return prevN
