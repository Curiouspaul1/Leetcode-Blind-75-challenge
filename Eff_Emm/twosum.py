class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
                """
        start = 0
        while  start <= len(nums)-1:
            sub = target - nums[start]
            for i in range(len(nums)):
                if nums[i] == sub and i != start:
                    return [i, start]
            start += 1

new = Solution()
print(new.twoSum([2,3,4],5))

