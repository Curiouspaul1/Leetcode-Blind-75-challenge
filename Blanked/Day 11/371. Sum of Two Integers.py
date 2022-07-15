
# https://leetcode.com/problems/sum-of-two-integers/
class Solution:
    def getSum(self, a: int, b: int) -> int:
        pos = []
        neg = []
        if a < 0:
            for i in range(abs(a)):
                neg.append(0)
        else:
            for i in range(a):
                pos.append(0)
        if b < 0:
            for i in range(abs(b)):
                neg.append(0)
        else:
            for i in range(b):
                pos.append(0)
        n = len(neg)
        while pos and n:
            pos.pop()
            n -= 1
        if n == 0:
            return len(pos)
        else:
            return n*(-1)
