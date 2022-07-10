class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1

        if len(nums) == 1:
            return nums[0]

        while lo < hi:
            md = (lo + hi) // 2
            if nums[md] > nums[hi]:
                lo = md+1
            else:
                hi = md

        return nums[lo]
