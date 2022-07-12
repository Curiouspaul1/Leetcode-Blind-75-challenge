class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()  # [-4, -1, -1, 0, 1, 2]
        
        for i, n in enumerate(nums):
            
            # check if this value is the same as the prev
            if i > 0 and n == nums[i-1]:
                continue   # next iteration of the loop
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                thSum = n + nums[left] + nums[right]
                
                if thSum < 0:
                    left += 1
                elif thSum > 0:
                    right -= 1
                else:
                    res.append([n, nums[left], nums[right]])
                    left += 1
                    
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
            
        return res