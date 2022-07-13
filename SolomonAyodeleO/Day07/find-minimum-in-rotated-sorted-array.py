# Approach 1 ==> O(n)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)

# Approach 2 ==> use binary search O(log n) - For one reason it was slower on leetcode 
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums)-1
        while l < h:
            mid = (l+h)//2
            if nums[mid] >= nums[h]:
                l = mid + 1
            else:
                h = mid
        return nums[l]