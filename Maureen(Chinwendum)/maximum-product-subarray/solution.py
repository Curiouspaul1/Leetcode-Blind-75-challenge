class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx = 1 
        mn = 1
        ans = float("-inf")
        
        for num in nums:
            mx, mn = max(num, mx*num, mn*num), min(num, mx*num, mn*num)
            ans = max(mx, mn, ans)
        return ans


                        
        
                
        
#Answer gotten from discussions