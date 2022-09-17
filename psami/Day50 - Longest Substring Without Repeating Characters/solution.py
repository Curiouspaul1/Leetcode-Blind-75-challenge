class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subtring = []
        gen=[]
        for i in s:
            if i not in subtring:
                subtring.append(i)
            else:
                gen.append([len(subtring),subtring])
                while i in subtring:
                    subtring = subtring[1:]
                subtring.append(i)

        gen.append([len(subtring),subtring])
        gen.sort()
        print(gen)
        return gen[-1][0]


x = Solution()
print(x.lengthOfLongestSubstring(

"pwwkew"))

