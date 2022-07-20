class Solution:
    def reverseBits(self, n: int) -> int:
        
        res=0
        
        for x in range(32):
            bit=(n>>x)&1
            res=res|(bit<<(31-x))
        return res
        