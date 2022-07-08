class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res = nums[0]
        cur = 0
        
        for n in nums:
            if cur < 0:
                cur = 0
            
            cur += n
            res = max(cur, res)
        
        
        return res
        
        