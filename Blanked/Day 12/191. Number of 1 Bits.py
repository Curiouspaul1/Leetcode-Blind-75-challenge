
# 

class Solution:
    def hammingWeight(self, n: int) -> int:
        c = Counter(bin(n)[2:])
        return c["1"]
        