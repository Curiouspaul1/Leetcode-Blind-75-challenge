class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum(map(lambda x: x == '1', bin(n)))
    def countBits(self, n: int) -> List[int]:
        return map(self.hammingWeight, range(n+1))
        
