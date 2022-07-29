
class Solution:
    def maxSubArray(self, nums):
        mainMax = max(nums)
        currentMax = 1
        currentMin = 1
        
        for number in nums:
            tempVar = currentMax * number
            currentMax = max(number, currentMax * number, currentMin * number)
            currentMin = min(number, tempVar, currentMin * number)
            mainMax = max(mainMax, currentMax)

        return mainMax
    
numList = [2,3,-2,4]
print(Solution().maxSubArray(numList))
