class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Method 1: T.C: O(n) S.C: O(n)
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        else:               
            maxcount = 0
            setnums = set(nums)
            for num in setnums:
                if num-1 not in setnums:
                    count = 0
                    while num + count in setnums:
                        count += 1
                    maxcount = max(count,maxcount)
            return maxcount
	   
	   # Method 2: T.C: O(nlogn+n) S.C: O(1)
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        else:            
            nums.sort()
            count = 1
            maxcount = 1
            for i in range(1,len(nums)):
                if nums[i] == nums[i-1]:
                    continue
                elif nums[i] == nums[i-1]+1:
                    count += 1
                else:
                    count = 1
                maxcount = max(count,maxcount)
            return maxcount
