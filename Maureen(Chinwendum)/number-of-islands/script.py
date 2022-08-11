class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r,c,ans = len(grid), len(grid[0]), 0
        
        def dfs(i,j, grid,r,c):
            if i<0 or j<0 or i>r-1 or j>c-1 or grid[i][j] != "1": # if the grid is out of range or not "1", return 
                return  
            
            grid[i][j] = "#"   # mark the visited gird so will not visit it again
            
            dfs(i+1, j, grid, r,c)  # visit up, down, right and left grids
            dfs(i-1, j, grid, r,c) 
            dfs(i, j+1, grid, r,c)
            dfs(i, j-1, grid, r,c)
           
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1": # dfs once find "1"
                    dfs(i,j, grid, r,c)
                    ans +=1  # find one more island
                    
        return ans