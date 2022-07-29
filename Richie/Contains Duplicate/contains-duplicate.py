class Solution:
    def containsDuplicate(self, nums):
        if len(list(set(nums))) == len(nums):
            return False
        else:
            return True

numList = [1,2,3,1]
print(Solution().containsDuplicate(numList))
