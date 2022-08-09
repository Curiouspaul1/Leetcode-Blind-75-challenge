class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        
        M = len(grid)
        N = len(grid[0])
        
        def dfs(i,j):
            
            if i<0 or i>=M or j<0 or j>=N or grid[i][j] != "1":
                return
            grid[i][j] = "0"
            
            dfs(i, j+1)
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j-1)
        
        for i in range(M):
            for j in range(N):
                
                if grid[i][j] == "1":
                    dfs(i,j)
                    count += 1
        return count
    
