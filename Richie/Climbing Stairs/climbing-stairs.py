class Solution:
    def climbStairs(self, n):
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
            
        return one
        
n = 5
print(Solution().climbStairs(n))
