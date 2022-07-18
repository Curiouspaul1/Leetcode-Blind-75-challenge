from ast import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        numsTotal = n *(n + 1) / 2
        numsSum = 0
        
        for num in nums:
            res += num
        
        return int(numsTotal - numsSum)