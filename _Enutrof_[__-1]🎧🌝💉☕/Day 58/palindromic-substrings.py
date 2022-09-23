class Solution:
    def isPalindromic(self, s, left, right):
        sub_count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            sub_count += 1
        return sub_count
    def countSubstrings(self, s: str) -> int: 
        count = 0
        for i in range(len(s)):
            count += self.isPalindromic(s, i, i)
            if i + 1 < len(s):
                count += self.isPalindromic(s, i, i + 1)
            
        return count
      
