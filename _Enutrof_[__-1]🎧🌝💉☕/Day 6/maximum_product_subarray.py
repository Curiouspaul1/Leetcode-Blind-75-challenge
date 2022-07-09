import numpy as np
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        queue = np.array([nums[0]])
        
        for i, num in enumerate(nums):
            if i == 0:
                continue
            try:
                queue = np.append([np.max(queue)], queue[-i:] * num)
            except:
                queue = queue[-i:] * num
            queue = np.append(queue, [num])
            
        return int(np.max(queue))
        
