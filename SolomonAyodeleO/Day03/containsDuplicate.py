# Approach 1 ==> O(n) space and time
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = collections.Counter(nums)
        for i in counter:
            if counter[i] > 1:
                return True
        return False

# Runtime: 868 ms, faster than 13.26% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 26 MB, less than 72.32% of Python3 online submissions for Contains Duplicate.


# Approach 2 ==> O(n) space and time
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

# Approach 3 ==> O(n) space and time
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) - len(nums)

# Approach 4 ==> O(n) space and time
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check=set()
        for val in nums:
            if val not in check:
                check.add(val)
            else:
                return True
        return False