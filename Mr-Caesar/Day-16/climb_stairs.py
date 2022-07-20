class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
#         edge cases
        memo[1] = 1
        memo[2] = 2
        def climb_stair(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = climb_stair(n - 1) + climb_stair(n-2)
                return memo[n]
        
        return climb_stair(n)
        