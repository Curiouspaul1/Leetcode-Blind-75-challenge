class Solution:
    def isPalindrome(self, s: str) -> bool:
        def check(st):
            listt = []
            listt[:] = st
            if "".join(reversed(listt)) == st:
                return True
            return False
            

        new_str = "".join(ch.lower() for ch in s if ch.isalnum())

        return check(new_str)
            
