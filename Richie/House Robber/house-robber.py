class Solution:
  def rob(self, nums):
    @cache
    def dp(i, prev):
      if i < 0:
        return 0
      ans = dp(i - 1, False)
      if not prev:
        ans = max(ans, dp(i - 1, True) + nums[i])
        
      return ans
    
    
    return dp(len(nums) - 1, False)
