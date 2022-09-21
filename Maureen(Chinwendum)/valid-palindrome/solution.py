class Solution:
    def isPalindrome(self, s: str) -> bool:

        l,r=0, len(s)-1
        while l < r:
            sl=s[l].lower()
            sr=s[r].lower()
            if sl not in 'abcdefghijklmnopqrstuvwxyz0123456789':
                l=l+1
                continue
            if sr not in 'abcdefghijklmnopqrstuvwxyz0123456789':
                r=r-1
                continue           
            
            if sl != sr:
                return False
            l=l+1
            r=r-1
        return True