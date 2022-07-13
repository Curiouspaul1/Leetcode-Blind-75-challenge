from ast import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left, right = 0, len(height) - 1
        res = 0
        
        # Area = length of shorter vertical line * distance between lines

        while left < right:
            shorterLine = min(height[left], height[right])
            distance = right - left

            area = shorterLine * distance
            res = max(area, res)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return res