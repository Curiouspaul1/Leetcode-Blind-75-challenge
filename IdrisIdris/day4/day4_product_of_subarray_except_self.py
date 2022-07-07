class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outputArr = [1]*len(nums)
        before = 1
        for i in range(len(nums)):
            outputArr[i] = before
            before *= nums[i]
        print(outputArr)
        after = 1
        for j in range(len(nums) - 1, -1, -1):
            outputArr[j] *= after
            after *= nums[j]
        return outputArr
