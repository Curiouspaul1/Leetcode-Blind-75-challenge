class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.dfs(0, 0, m, n, {})
        
    def dfs(self, row, col, m, n, memo):
        id = col + row * n
        
        if row == m-1 and col == n-1:
            memo[id] = 1
        elif row >= m or col >= n:
            memo[id] = 0
        
        if id not in memo:    
            memo[id] = self.dfs(row+1, col, m, n, memo) + self.dfs(row, col+1, m, n, memo)
        return memo[id]
