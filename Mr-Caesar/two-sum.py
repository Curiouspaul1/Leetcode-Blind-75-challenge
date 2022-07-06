class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashMap = {}
        
    for index,value in enumerate(nums):
      df = target - value
      if df in hashMap:
          return [hashMap[df], index]
      hashMap[value] = index
    return                        