
# https://leetcode.com/problems/reverse-bits/submissions/

class Solution:
    def reverseBits(self, n: int) -> int:
        
        n =  str(bin(n)[2::])
        n = n[::-1]
        b = (32 - len(n))*'0'
    
        if b:
            n +=b
        
        return int(n,2)