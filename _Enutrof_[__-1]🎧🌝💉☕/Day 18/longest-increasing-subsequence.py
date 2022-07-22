class Solution:        
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    cache[i] = max(cache[i], 1 + cache[j])
        return max(cache)
      
