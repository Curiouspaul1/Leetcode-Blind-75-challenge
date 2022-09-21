class Solution:
    def isValid(self, s: str) -> bool:
        para_store={'(':')', '[':']', '{':'}'}
        stack=[]
        for i in s:
            if i not in para_store:
                if stack and para_store[stack[-1]] == i:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
                
            