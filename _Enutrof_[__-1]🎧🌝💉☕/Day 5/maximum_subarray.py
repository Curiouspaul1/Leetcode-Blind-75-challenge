class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pos = 0
        length = len(nums)
        start = pos
        maxi = -1e10
        curr = 0
        while pos < length:
            curr += nums[pos]
            if curr <= 0 or curr - nums[start] > curr:
                start = pos
                curr = nums[pos]
            if curr > maxi:
                maxi = curr
            pos += 1
        return (maxi)
      
