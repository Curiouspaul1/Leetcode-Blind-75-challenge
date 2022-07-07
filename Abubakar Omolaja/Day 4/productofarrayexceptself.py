class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums)==0:
            return []
        n = len(nums)
        result = [0 for i in range(len(nums))]
        result[0]=1
        rp = 1
        for i in range(1,n,1):
            rp = rp *nums[i-1]
            result[i] = rp
        rp = 1
        for i in range(n-2,-1,-1):
            rp = rp * nums[i+1]
            result[i] = result[i]*rp
        return result