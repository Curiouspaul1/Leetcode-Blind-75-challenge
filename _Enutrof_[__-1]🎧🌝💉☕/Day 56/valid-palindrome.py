class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        alnum = set(string.ascii_letters + string.digits)
        
        while i < j:
            while not s[i] in alnum and i + 1 < j:
                i += 1
            while not s[j] in alnum and j - 1 > i:
                j -= 1
                
            if {s[j], s[i]} <= alnum and s[i].lower() != s[j].lower():
                return False
            i += 1
            j  -= 1
        return True
