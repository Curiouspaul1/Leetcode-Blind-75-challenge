class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxP, minP = 1,1
        res = max(nums)
        
        for n in nums:
            if n == 0:
                maxP, minP = 1,1
                continue
            
            temp = n * maxP
            maxP = max(n*maxP, n*minP, n)
            minP = min(temp, n*minP, n)
            res = max(maxP, res)
        
        return res