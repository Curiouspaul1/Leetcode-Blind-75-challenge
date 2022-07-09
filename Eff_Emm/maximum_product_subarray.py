class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mins = maxi =1
        result = max(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                mins = maxi =1
            temp = maxi * nums[i]
            maxi = max(nums[i] * maxi,nums[i]* mins, nums[i])
            mins = min(temp,nums[i], mins*nums[i])
            result = max(result,maxi)
        return result