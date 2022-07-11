class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            
            if nums[left] <= nums[middle]:
                if target >= nums[left] and target <= nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            
            else:       #  [5,1,2,3,4]
                if target <= nums[right] and target >= nums[middle]:
                    left = middle + 1
                else:
                    right = middle - 1
        return -1





    
# class Solution:
#     def search(self, nums, target):
#         l, r = 0, len(nums)-1
#         while l <= r:
#             mid = l + (r-l)//2
#             if nums[mid] == target:
#                 return mid
#             if nums[left] <= nums[mid]:  # here should include "==" case
#                 if nums[left] <= target < nums[mid]:      target >= nums[left] and target <= nums[middle]
#                     r = mid - 1
#                 else:
#                     left = mid + 1
#             else:
#                 if nums[mid] < target <= nums[r]:
#                     l = mid + 1
#                 else:
#                     r = mid - 1
#         return -1
    
    

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         pivot = 0
#         # We need to find the index at which the pivot occurs
#         for i in range(1, len(nums)):
#             if nums[i-1] > nums[i]:
#                 pivot = i
#                 break

#         # To get to the pivoted index we need to do (i + pivot) % len(nums)
#         # perform binary search on the array 
#         start = 0
#         end = len(nums) - 1
        
#         while start <= end:
#             mid = (start + end) // 2
#             pivoted_mid = (mid + pivot) % len(nums)
#             if nums[pivoted_mid] == target:
#                 return pivoted_mid
#             elif nums[pivoted_mid] > target:
#                 end = mid - 1
#             else:
#                 start = mid + 1
#         return -1
    
# class Solution(object):
#     def search(self, nums, target):
#         left, right = 0, len(nums) - 1
#         while left <= right:
#             mid = (left + right) >> 1
#             if nums[mid] == target:
#                 return mid
#             if target >= nums[0]:
#                 if nums[mid] < target and nums[mid] >= nums[0]:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#             else:
#                 if nums[mid] < target or nums[mid] >= nums[0]:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#         return -1    