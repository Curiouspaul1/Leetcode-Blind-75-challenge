class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix    
            prefix *= nums[i]
        
        # after prefix operation: res = [1,1,2,6]
        
        postfix = 1
        for i in range(len(nums) -1, -1, -1): #Start at end of array
            res[i] *= postfix
            postfix *= nums[i]
        
        # after postfix: res = [24,12,8,6]
            
        return res