class Solution:
    def missingNumber(self, nums):
        nums = set(nums)
        completeNums = set(range(0, len(nums) + 1))
        return list(completeNums - nums)[0]

numberList = [0,1,2,4,5,6,7]
print(Solution().missingNumber(numberList))
