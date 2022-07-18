class Solution:
    def missingNumber(self, nums) :
        for i in range(len(nums)):
            if i not in nums:
                return i 
            
        return len(nums)
        