class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
            hashset=set()
            for x in nums:
                if x not in hashset:
                    hashset.add(x)
                    continue
                return True
            return False
        