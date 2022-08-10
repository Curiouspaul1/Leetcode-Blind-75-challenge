class Solution:
    def longestConsecutive(self, nums):
        nums.sort()
        if not nums:
            return 0
        unique = [nums[0]]
        
        for i in range(1,len(nums)):
            if nums[i] != unique[-1]:
                unique.append(nums[i])
                
        length = 0
        maxlength = 0
        for i in range(len(unique)):
            if i > 0 and unique[i] == unique[i-1]+1:
                length+=1
            else:
                length = 1
            maxlength = max(maxlength,length)
        return maxlength
