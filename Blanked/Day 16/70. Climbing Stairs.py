
# https://leetcode.com/problems/climbing-stairs/submissions/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n ==1:
            return 1
        x, y = 1, 1    
        
        for i in range(1,n):
            temp = x
            x = x+y
            y =temp
            
        return x