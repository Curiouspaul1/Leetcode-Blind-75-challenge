class MySolution:
    def longestPalindrome(self, s: str) -> str:
        str_length = len(s)

        def check(st):
            listt = []
            listt[:] = st
            if "".join(reversed(listt)) == st:
                return True
            return False

        if check(s):
            return s

        for j in range(str_length):
            for i in range(j+1):
                subs = s[i:str_length-j+i]
                if check(subs):
                    return subs
        return ""

 



class Solution:
    def longestPalindrome(self, s: str) -> str:
        str_length = len(s)
        max_length = 0
        max_str = ""

        for i in range(str_length):
            #odd
            l,r = i,i

            while l>= 0 and r<str_length and s[l] == s[r]:
                if (r-l+1) > max_length:
                    max_length=(r-l+1)
                    max_str = s[l:r+1]
                l -= 1
                r += 1

            #even
            l,r=i,i+1
            while l>= 0 and r<str_length and s[l] == s[r]:
                if (r-l+1) > max_length:
                    max_length=(r-l+1)
                    max_str = s[l:r+1]
                l -= 1
                r += 1
        return max_str



        
x = Solution()
x.longestPalindrome("1234567")

        
        
