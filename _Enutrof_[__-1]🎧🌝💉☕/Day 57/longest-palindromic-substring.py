class Solution:
    def longestPalindrome(self, s: 'str') -> 'str':
        if len(s) <= 1:
            return s
        start = 0
        end = 0
        
        for i in range(len(s)):
            max_len = max(
                self.fromWithin(s, i, i + 1), 
                self.fromWithin(s, i, i)
            )
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + (max_len // 2)
        return s[start: end+1]
        
    def fromWithin(self, s, left, right):
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            
        return right - left - 1
      
