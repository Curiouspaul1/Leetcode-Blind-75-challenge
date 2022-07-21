class Solution:
    def climbStairs(self, n: int) -> int:
        
        l=1
        r=1
        for x in range(n-1):
            temp=l
            l=l+r
            r=temp
        return l
            
            
        