class Solution:
    def __init__(self):
        self.d = {0: 0, 1: 1}
    def fib(self, n: int) -> int:
        if n in self.d:
            return self.d[n]            
        else:
            x = self.fib(n-1)
            self.d[n-1] = x
            y = self.fib(n-2)
            self.d[n-2] = y
            if n > 2:
                del self.d[n-3]
            return x + y
    def climbStairs(self, n: int) -> int:
        return self.fib(n+1)
    
    # results:   0 1 1 2 3 5 8 13 21
    #      n:      0 1 2 3 4 5  6  7
    # fibonacci: 0 1 2 3 4 5 6  7  8
        
