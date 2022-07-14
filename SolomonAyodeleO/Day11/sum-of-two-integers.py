# Approach 1 ==> Using Mathematic Logarithm - O(1) time, space unknown
class Solution:
    def getSum(self, a: int, b: int) -> int:
        return int(math.log2(2**a * 2**b)) # Using Logarithm addition

