import numpy as np
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = np.unique(nums)
        if nums.shape[0] <= 1:
            return nums.shape[0]
        count = 0
        max_count = 0
        i = 0
        while i < nums.shape[0]-1:
            if (nums[i+1] - nums[i]) == 1:
                count += 1
            else:
                if count > max_count:
                    max_count = count
                count = 0
            i+=1
        if count > max_count:
            max_count = count
        return max_count + 1

                
        
