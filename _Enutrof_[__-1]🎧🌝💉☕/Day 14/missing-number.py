class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = lambda x: int(x/2 * (2*1 + (x - 1)*1))
        return int(total(len(nums)) - sum(nums))
        #a = {i for i in range(0, len(nums)+1)}.difference(nums)
        #return tuple(a)[0]
        
