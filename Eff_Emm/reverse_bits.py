class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            bits = (n >> i ) & 1
            res = res | (bits <<(31-i))
        return res