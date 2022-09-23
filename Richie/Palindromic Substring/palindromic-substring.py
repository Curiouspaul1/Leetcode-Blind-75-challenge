class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        i = 0
        while(i < n) :
            ch = s[i]
            j = i            
            while(j < n and s[i] == s[j]) :
                j += 1
            reps = j - i
            count += (reps * (reps+1))//2
            l = i - 1
            r = j
            i = j

            while(l>=0 and r < n and s[l] == s[r]) :
                count += 1
                l -= 1
                r += 1
            #print(count)
            #well thats it!

        return count
