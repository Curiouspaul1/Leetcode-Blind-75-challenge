


from operator import indexOf


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        currentguy = ""
        smallest_length = float("infinity")
        def checkAbc(substring: str):
            count = 0
            subList = []
            subList[:]=substring
            if len(substring) >= len(t):
                for x in range(len(t)):
                    if t[x] in subList:
                        count +=1
                        subList.remove(t[x])

                if count == len(t): 
                    if len(substring) < smallest_length:
                        return (len(substring), substring)
            return smallest_length, currentguy


        for j in range(1,len(s)+1):
            subs = ""
            for i in range(j, len(s)+1):
                n =  i -1;
                subs = subs + s[n];
                smallest_length, currentguy = checkAbc(subs);

        return currentguy
  

x = Solution()
s, t = "bbaa", "aba"
print(x.minWindow(s, t))