class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum(map(lambda x: x == '1', bin(n)))
        
