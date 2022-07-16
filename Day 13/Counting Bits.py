from ast import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        
        array = [0] * (n + 1)
        offset = 1        
        
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
                
            array[i] = 1 + array[i - offset]
            
        return array
            
        

            
#   0:      0 0 0 0
#   1:      0 0 0 1   1 + dp[n - 1]
#   2;      0 0 1 0   1 + dp[n - 2]
#   3:      0 0 1 1   1 + dp[n - 2]
#   4:      0 1 0 0                   1 + dp[n - 4]
#   5:      0 1 0 1                   1 + dp[n - 4]
#   6:      0 1 1 0                   1 + dp[n - 4]
#   7:      0 1 1 1                   1 + dp[n - 4]
    
#   8:      1 0 0 0                   1 + dp[n - 8]
#   9:      1 0 0 1                   1 + dp[n - 8]
#   10:     1 0 1 0                   1 + dp[n - 8]
#   11;     1 0 1 1                   1 + dp[n - 8]
#   12:     1 1 0 0                   1 + dp[n - 8]
#   13:     1 1 0 1                   1 + dp[n - 8]
#   14:     1 1 1 0                   1 + dp[n - 8]
#   15;     1 1 1 1                   1 + dp[n - 8]
  