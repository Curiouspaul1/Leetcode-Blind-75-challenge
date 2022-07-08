from ast import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        print(sum(nums))
        maxSub = nums[0]
        curSum = 0
        for i in nums:
            if curSum < 0:
                curSum = 0
            curSum += i
            maxSub = max(curSum, maxSub)
        return maxSub
