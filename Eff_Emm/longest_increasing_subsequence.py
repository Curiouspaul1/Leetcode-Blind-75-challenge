class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        holder = [1] * len(nums)
        before = 0
        after = 1
        
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    holder[i] = max(holder[i],1+ holder[j])
                    
        return max(holder)
                    