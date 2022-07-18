class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tot = 0
        nex = 0
        
        for i in range(len(nums)+1):
            tot += i
            
        for i in range(len(nums)):
            nex += nums[i]
        return tot -  nex
            
            