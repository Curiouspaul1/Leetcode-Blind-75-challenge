class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque([])
        matching = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in ')}]' and stack:
                if matching[char] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        return not bool(stack)
      
