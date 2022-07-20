class Solution:
    def climbStairs(self, n: int) -> int:
        
        curr = 1
        prev = 1
        
        for i in range(n-1):        
            temp = curr
            curr = curr + prev
            prev = temp
        
        return curr