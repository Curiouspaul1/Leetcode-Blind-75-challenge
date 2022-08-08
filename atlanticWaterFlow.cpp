class Solution {
public:
    vector<vector<bool>> atlantic,pacific;
    vector<vector<int>>ans;
    int row_offsets[4]={0,1,0,-1};
    int col_offsets[4]={1,0,-1,0};
    void markCells(vector<vector<int>>&heights,int x,int y,int last,vector<vector<bool>>&vis)
    {   
        if(x<0||y<0||x>=heights.size()||y>=heights[0].size()||heights[x][y]<last||vis[x][y]==1)return;
        vis[x][y]=1;
        if(pacific[x][y]&&atlantic[x][y])ans.push_back({x,y});
        for(int i =0;i<4;i++)
            markCells(heights,x+row_offsets[i],y+col_offsets[i],heights[x][y],vis);
    }
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int n(heights.size()),m(heights[0].size());
        atlantic.resize(n,vector<bool>(m,0));
        pacific.resize(n,vector<bool>(m,0));
        for(int col =0;col<m;col++)markCells(heights,0,col,0,pacific),markCells(heights,n-1,col,0,atlantic);
        for(int row =0;row<n;row++)markCells(heights,row,0,0,pacific),markCells(heights,row,m-1,0,atlantic);
        return ans;
    }
};
