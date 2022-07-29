
class Solution:
    def maxSubArray(self, nums):
        mainMax = float('-inf')
        currentMax = 0
        
        for  i in range(len(nums)):
            number = nums[i]
            currentMax = max(currentMax + number, number)
            mainMax = max(mainMax, currentMax)
            
        return mainMax
    
numList = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(numList))
