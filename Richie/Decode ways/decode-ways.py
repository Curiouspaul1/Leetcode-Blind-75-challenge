class Solution:
    def numDecodings(self, s, memo = {}):
        if s in memo:
            return memo[s]
        if s and s[0] == "0":
            return 0
        if len(s)<= 1:
            return 1
        
        sn, dn = int(s[:1]), int(s[:2])
        
        result = self.numDecodings(s[1:]) 
        
        if 27>dn>0:
            result += self.numDecodings(s[2:]) 
        memo[s] = result
        return result
                     
