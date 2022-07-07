# https://leetcode.com/problems/product-of-array-except-self/submissions/


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        
        pre_fix = 1
        for i in range(len(nums)):
            res[i] = pre_fix
            pre_fix *= nums[i]
        post_fix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post_fix
            post_fix *= nums[i]
        return res