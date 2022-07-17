class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[0]*(n+1)
        for i in range(n+1):
            ans[i]=ans[i>>1]+(i&1)
        return ans
#Idea is if you if you double a number, left shift, you would get the sane number of 1's plus 1 if the number is odd
    
