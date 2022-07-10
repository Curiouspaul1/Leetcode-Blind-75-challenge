#Reference: https://www.youtube.com/watch?v=2MmGzdiKR9Y&t=1s



import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        total=0
        max_total=-sys.maxsize
        for x in range(len(nums)):
            total+=nums[x]
            if total<=nums[x]:
                total=nums[x] 
            if total > max_total:
                max_total=total
        return max_total
                
        