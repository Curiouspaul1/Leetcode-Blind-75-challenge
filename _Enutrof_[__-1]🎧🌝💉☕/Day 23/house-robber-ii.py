class Solution:
    def rob_(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 2)
        for i in range(len(nums)-1, -1, -1):
            dp[i] = nums[i] + max(dp[i+2:])
        return max(dp[0:2])
        
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_(nums[1:]), self.rob_(nums[:-1]))
        
        
