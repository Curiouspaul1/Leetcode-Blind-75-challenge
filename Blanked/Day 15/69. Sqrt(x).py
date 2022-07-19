
#  https://leetcode.com/problems/sqrtx/
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x
        
        if x < 2:
            return x
        
        while left < right:
            mid = left + (right-left)//2
            
            if mid*mid == x:
                return mid
            elif mid*mid > x:
                right = mid
            elif mid*mid < x:
                left = mid+1
                
        return left-1
        