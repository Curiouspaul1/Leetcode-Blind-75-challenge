class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) -1
        result = 0
        start = 0
        
        while left < right:
            area = min(height[left], height[right]) *( right-left)
            result = max(result, area)
            
            if height[right] > height[left]:
                left += 1
                
            elif height[left] > height[right]:
                right -= 1
            else:
                right -=1
            
            
        return result
            