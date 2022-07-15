class Solution:
    def hammingWeight(self, n: int) -> int:
        out = 0
        while n !=0:
            if n%2==1:
                out = out + 1
                
            n>>=1
            
        return out

var = 000000000000000000000001011
print(Solution().hammingWeight(var))
