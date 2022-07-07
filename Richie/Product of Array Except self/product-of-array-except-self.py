import math
class Solution:
    def productExceptSelf(self, nums):
        productList = []
        usedNumbers = {}
        for i in range(len(nums)):
            originalNumber = nums[i]
            nums[i] = 1
            if originalNumber not in usedNumbers:
                usedNumbers[originalNumber] = math.prod(nums)

            productList.append(usedNumbers[originalNumber])    
            nums[i] = originalNumber
            
        return productList

numList = [1,2,3,4]
print(Solution().productExceptSelf(numList))
