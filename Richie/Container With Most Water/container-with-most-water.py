class Solution:
    def maxArea(self, height):
        maxArea = 0
        l = 0
        r = len(height) - 1
        
        while l < r:
            currArea = min(height[l], height[r]) * (r - l)
            maxArea = max(currArea, maxArea)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return maxArea



myList = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(myList))
