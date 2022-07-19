class Solution:
    def reverseBits(self, n: int) -> int:
        b = bin(n)[2:]
        b = b.zfill(32)
        return int(b[::-1], 2)
    
