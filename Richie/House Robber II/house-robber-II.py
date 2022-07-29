class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        a1 = 0
        b1 = nums[0]
        a2 = 0
        b2 = nums[1]
        for i in range(1, len(nums) - 1):
            a1, b1 = b1, max(a1 + nums[i], b1)
            a2, b2 = b2, max(a2 + nums[i + 1], b2)
        return max(b1, b2)
