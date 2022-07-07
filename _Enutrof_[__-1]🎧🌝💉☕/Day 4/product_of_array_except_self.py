class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]
        suffix = 1
        for num in nums:
            output.append(output[-1] * num)
        output[-1] = 1
        
        for i, num in enumerate(nums, start=1):
            try:
                output[-i] = output[-i-1] * suffix 
                suffix *= nums[-i]
            except:
                continue

        return output[1:]
        
