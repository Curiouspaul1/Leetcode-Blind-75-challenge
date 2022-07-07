
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check = {}
        for i in nums:
            if i in check:
                return True
            else:
                check[i] = i
                
        return False
                