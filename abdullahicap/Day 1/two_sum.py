def twoSum(nums, target):
        le = len(nums)
        for i in range(le):
            for j in range(i):     
                if nums[i]+nums[j]==target: return [i,j]

