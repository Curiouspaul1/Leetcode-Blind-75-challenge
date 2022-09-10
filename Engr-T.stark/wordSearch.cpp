class Solution {
public:
    bool find=false;
    void dfs(vector<vector<bool>> &vis,vector<vector<char>>& board, string word,int i,int j,int c){
        if(c>=word.length()) {
            find=true;
                             return;}
        if( i<0 || j<0 || i>=board.size() || j>=board[0].size()|| vis[i][j] || find) return;
        vis[i][j]=true;
        
        if(word[c]==board[i][j]){
        dfs(vis,board,word,i+1,j,c+1);
            dfs(vis,board,word,i,j+1,c+1);
            dfs(vis,board,word,i-1,j,c+1);
            dfs(vis,board,word,i,j-1,c+1);
            }
    vis[i][j]=false;
    }
    bool exist(vector<vector<char>>& board, string word) {
           vector<vector<bool>> vis( board.size() , vector<bool> (board[0].size(),false)); 
        

        for(int i=0;i<board.size();i++){
            for(int j=0;j<board[0].size();j++){
                if(find==true) return true;
                if(!vis[i][j]){
                    dfs(vis,board,word,i,j,0);
                }
                
             
                
            }
        }
        return find;
    }
};
