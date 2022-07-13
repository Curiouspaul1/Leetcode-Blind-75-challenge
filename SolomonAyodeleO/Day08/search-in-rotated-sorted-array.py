# Approach 1 - normal linear search O(n)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1



# Approach 2 - using binary search O(log n) with OR condition
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right: 
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]: 
                if target < nums[left] or target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else: 
                    left = mid + 1
        return -1

# Approach 3 - Same binary search with AND condition
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = (left + right)//2
            if nums[pivot] == target:
                return pivot
            elif nums[pivot] >= nums[left]:
                if target >= nums[left] and target < nums[pivot]:
                    right = pivot - 1
                else:
                    left = pivot + 1
            else:
                if target <= nums[right] and target > nums[pivot]:
                    left = pivot + 1
                else:
                    right = pivot - 1
                    
        return -1
        