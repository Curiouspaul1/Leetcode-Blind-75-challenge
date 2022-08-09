class Solution {
public:
    int area(int r,int c,vector<vector<char>>& grid){
        if(r < 0 || r >=grid.size() || c<0 || c >=grid[0].size() || grid[r][c] == '0')
            return 0;
        grid[r][c] = '0';
        return (1 + area(r+1,c,grid) + area(r-1, c,grid) + area(r, c-1,grid) + area(r, c+1,grid));
    }    
    
    int numIslands(vector<vector<char>>& grid){
        int ans = 0,res =0;
        for(int i= 0;i<grid.size();i++){
            for(int j=0;j<grid[0].size();j++){
                ans = area(i,j,grid);
                if(ans>0) res++;
            }
        }
        return res;
    }
};
