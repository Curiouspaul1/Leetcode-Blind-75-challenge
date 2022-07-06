class Solution(object):
    def twoSum(self, nums, target):
        for i,val in enumerate(nums):

            if target - val in nums:

                if target - val == val and nums.count(val) == 1:
                    continue
                elif target - val == val and nums.count(val) > 1:
                    return [i, nums.index(target-val, i+1)]

                return [i, nums.index(target-val)]


