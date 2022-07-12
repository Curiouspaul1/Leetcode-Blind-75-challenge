class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
                
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = n + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l +=1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l+=1
        return res

print(Solution().threesum([-1,0,1,2,-1,-4]))
