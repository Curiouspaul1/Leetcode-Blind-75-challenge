class Solution:
    def countSubstrings(self, s: str) -> int:
        str_length = len(s)
        count = 0

        for i in range(str_length):
            #odd
            l,r = i,i

            while l>= 0 and r<str_length and s[l] == s[r]:
                count+=1
                l -= 1
                r += 1

            #even
            l,r=i,i+1
            while l>= 0 and r<str_length and s[l] == s[r]:
                count +=1
                l -= 1
                r += 1
        return count


x =Solution()
print(x.countSubstrings("aaa"))
