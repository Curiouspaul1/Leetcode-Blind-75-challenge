class Solution:
    def reverseBits(self, n):
        ans = 0
        for i in range(1, 33):
            ans <<=1
            ans = ans|(n % 2)
            n >>=1
            
        return ans

bit = 00000010100101000001111010011100
print(Solution().reverseBits(bit))
