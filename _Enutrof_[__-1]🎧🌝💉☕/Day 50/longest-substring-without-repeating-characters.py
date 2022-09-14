class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        start = 0
        end = 1
        charSet = {s[0]: 0}
        maximum = end - start
        while end < len(s):
            if s[end] in charSet:
                start = charSet[s[end]] + 1
                end += 1
                charSet = {s[i]: i for i in range(start, end)}
            else:
                charSet[s[end]] = end
                end += 1
            if (end - start) > maximum:
                maximum = end - start
        return maximum
        
