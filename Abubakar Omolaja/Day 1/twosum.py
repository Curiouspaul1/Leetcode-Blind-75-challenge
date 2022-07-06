class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for k, v in enumerate(nums):
            num = target - v
            if num in dict1:
                return (dict1[num],k)   
            else:
                dict1[v] = k