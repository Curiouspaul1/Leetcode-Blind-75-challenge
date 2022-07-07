class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1, nums[-1]]
        for i, num in enumerate(nums):
            prefix.append(prefix[-1] * num)
            try:
                suffix.append(suffix[-1] * nums[-(i+2)])
            except:
                suffix.pop()

        return [prefix[i] * suffix[-i-1] for i, num in enumerate(nums)]
        
