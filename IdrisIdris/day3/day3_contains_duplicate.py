from ast import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numSet = set(nums)
        if len(numSet) != len(nums):
            return True
        else:
            return False
