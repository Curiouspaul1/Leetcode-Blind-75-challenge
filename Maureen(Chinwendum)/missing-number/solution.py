class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        length=len(nums)
        
#         summ=0
#         for x in range(length+1):
            
#             summ+=x
            
#         sum_real=0    
#         for x in nums:
#             sum_real+=x
            
#         return summ-sum_real

        for i,v in enumerate(nums):
            print('i:'+str(i))
            print('v'+str(v))
            
            length^=i
            length^=v
            print('length:'+str(length))
        return length
            
            
        