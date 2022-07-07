# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_range = 0
        max_sum = nums[0]

        for i in range(len(nums)):
            max_range += nums[i]
            if max_sum < max_range:
                max_sum = max_range
            if max_range < 0:
                max_range = 0

        return max_sum
