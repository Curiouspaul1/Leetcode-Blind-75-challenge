class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = nums[0]
         
        for num in nums:
            if currSum < 0:
                currSum = 0
            currSum += num
            maxSum = max(maxSum, currSum)
        return maxSum              