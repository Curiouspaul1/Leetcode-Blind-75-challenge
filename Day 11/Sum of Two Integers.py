import math


class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        a1 = math.pow(2,a)
        a2 = math.pow(2,b)
        
        prod = a1 * a2
        return int(math.log2(prod))   
    
#     Using Exponents and Log
#     a^m x a^n = a^(m+n)
#     we know that loga(a^n) = n
#     loga(a^(m+n)) = m + n