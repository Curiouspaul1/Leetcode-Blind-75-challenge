import sys
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l,r=0,len(height)-1
        max_=-sys.maxsize
        while l<r:
            if height[l]>height[r]:
                product=(r-l)*height[r]
                r=r-1
            else:
                product=(r-l)*height[l]
                l=l+1
            if product>max_:
                max_=product
        return max_
            
        