class Solution {
public:
    
    
    int f(int n , int T, vector<int>&coin,vector<vector<int>>&dp){
        
        //base case
        if(n==0){
            if(T%coin[n]==0){
                return (T/coin[n]);
            }
            return 1e9;
        }
        
        if(dp[n][T]!=-1){
            return dp[n][T];
        }
        
        
        int not_take = f(n-1,T,coin,dp);
        int take =INT_MAX;
        
        if(coin[n]<=T){
            take= 1+f(n,T-coin[n],coin,dp);
        }
        
        return dp[n][T] = min(take,not_take);
        
    }
    
    int coinChange(vector<int>& coins, int amount) {
        
        int n = coins.size();
    
        vector<vector<int>>dp(n+1, vector<int>(amount+1,0));
        
        for(int i =0; i<amount+1; i++){
            if(i%coins[0]==0){
                dp[0][i] = i/coins[0];
            }
            else{
                dp[0][i] = 1e9;
            }
            
        }
        
        for(int  i =1; i<n; i++){
            for(int j =0; j<amount+1; j++){
                int not_take = dp[i-1][j];
                int take =INT_MAX;

                if(coins[i]<=j){
                    take= 1+dp[i][j-coins[i]];
                }

                dp[i][j] = min(take,not_take);
            }
        }
        
            int ans =dp[n-1][amount];
        if(ans==1e9){
            ans =-1;
        }
        return ans;
       
      
    }
};
