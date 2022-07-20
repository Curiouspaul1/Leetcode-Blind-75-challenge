class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = n>>i & 1
            res = res | bit<<(32-1-i)
            
        return res