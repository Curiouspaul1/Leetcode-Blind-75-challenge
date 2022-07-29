class Solution:
    def findMin(self, nums):
        return sorted(nums)[0]
    
numList = [2,3,-2,4]
print(Solution().findMin(numList))
