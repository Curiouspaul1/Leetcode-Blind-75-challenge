class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        present = 0
        maxs = nums[0]
        
        for i in nums:
            if present < 0:
                present = 0
            present += i
            maxs = max(present, maxs)
        return maxs