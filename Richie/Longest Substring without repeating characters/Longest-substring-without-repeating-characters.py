class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_len = len(s)
        
        if str_len == 0:
            return 0
        if str_len == 1:
            return 1
        
        l, r = 0, 1
        longest = 0
        substr = set()
        substr.add(s[l])
        
        while r < str_len:
            longest = max(longest, r - l)

            if s[r] in substr:
                substr.remove(s[l])
                l += 1
                continue
            substr.add(s[r])
            r += 1
        
        longest = max(longest, r - l)
        return longest
            
            
