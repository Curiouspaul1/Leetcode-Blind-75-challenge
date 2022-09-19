class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_ch = ["(", "{", "["]
        closed_ch = [")", "}", "]"]
        match = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        for ch in s:
            if ch in closed_ch and len(stack) == 0:
                return False
            if ch in closed_ch and match[ch] == stack[-1]:
                stack.pop()
                continue
                
            stack.append(ch)
        
        return len(stack) == 0
        
#

