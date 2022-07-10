class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums
        start = 0
        stop = len(nums)
        while start < stop:
            mid = (start + stop) // 2
            if nums[mid] > nums[-1]:
                start = mid + 1
            else:
                stop = mid
                
        return nums[start]
        
