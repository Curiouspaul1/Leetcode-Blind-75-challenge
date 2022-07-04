class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_ ={}
        for i,j in enumerate(nums):
            compliment = target -j
            if compliment not in dict_:
                dict_[j] = i
            else:
                return [dict_[compliment], i]
