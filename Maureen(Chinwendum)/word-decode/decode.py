class Solution:
    n=0
    def numDecodings(self, s):

        self.actual_func(s, 0)
        res=self.n
        self.n=0
        return res
    
    def actual_func(self, s, i):
            if i>len(s)-1:
                self.n=self.n+1
                return 
            if s[i]=="0":
                return
            self.actual_func(s,i+1)
            
            if i+1 < len(s) and (s[i]=="1" or (s[i]=="2" and s[i+1] in "0123456")):
                self.actual_func(s,i+2)
            

check=Solution()
print(check.numDecodings("111111111111111111111111111111111111111111111"))