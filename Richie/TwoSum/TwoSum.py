class Solution:
    def twoSum(self, nums, target):
        ans = []
        for i in range(len(nums)):
            test = target - nums[i]
            nums[i] = str(nums[i])
            if test in nums:
                return [i, nums.index(test)]
            else:
                nums[i] = int(nums[i])

numberList = [3,2,4]
print(Solution().twoSum(numberList, 6))
