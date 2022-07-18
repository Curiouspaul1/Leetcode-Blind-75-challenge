# https://leetcode.com/problems/counting-bits/submissions/

class Solution:
    def countBits(self, n: int):
        ans = []
        for i in range(n+1):
            b = bin(i)
            ans.append(str(b).count("1"))
        return ans
        