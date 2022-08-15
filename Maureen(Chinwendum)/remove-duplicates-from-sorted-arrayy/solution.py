class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        newnums = []
        for i in nums:
            if i not in newnums:
                newnums.append(i)
        nums.clear()
        nums.extend(newnums)