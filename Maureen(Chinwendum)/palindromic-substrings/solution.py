class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        for i in range(len(s)):
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                count=count+1
                l=l-1
                r=r+1
        for i in range(len(s)):
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                count=count+1
                l=l-1
                r=r+1
        return count
                
        