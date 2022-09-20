class Solution:
    def isValid(self, s: str) -> bool:
        stack = []


        groups ={
            ")": "(",
            "]":"[",
            "}": "{",
        }


        for i in s:
            if i in groups:
                if stack and  stack[-1] == groups[i]:
                    stack.pop()
                else: return False
            else:
                stack.append(i)
        return True if not stack else False


x = Solution()
ss = x.isValid("{[]}")

print(ss)