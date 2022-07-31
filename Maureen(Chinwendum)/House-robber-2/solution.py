class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0], nums[1])
        
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        x=2
        max_=-sys.maxsize
        res=[nums[0]]
        if nums[1]>nums[0]:
            res.append(nums[1])
        else:
            res.append(nums[0])
        while x<len(nums):
            max_=max(res[x-2]+nums[x], res[x-1])
            res.append(max_)
            x=x+1
        return max(res)
        