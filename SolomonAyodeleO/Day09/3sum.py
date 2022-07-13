# Approach 1 -
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # O(n) in python due to Timsort

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            j, k = i+1, len(nums) - 1
        
            while j < k:
                currSum = nums[i] + nums[j] + nums[k]
                if currSum > 0:
                    k -= 1
                elif currSum < 0:
                    j += 1
                else:
                    if not [nums[i], nums[j], nums[k]] in res:
                        res.append([nums[i], nums[j], nums[k]])
                    j += 1
        return res


# Approach 2 - 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # O(n) in python due to Timsort

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            j, k = i+1, len(nums) - 1
        
            while j < k:
                currSum = nums[i] + nums[j] + nums[k]
                if currSum > 0:
                    k -= 1
                elif currSum < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        return res