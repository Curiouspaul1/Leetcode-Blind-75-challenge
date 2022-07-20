class Solution {

public:

    int climbStairs(int n) {

    vector<int> dp(n+1,-1);

      return Memo(n,dp);

    }

   int Memo(int n, vector<int>&dp){

        if(n<=2) return n;

        if(dp[n] != -1) return dp[n];

        return dp[n] = Memo(n-1,dp) + Memo(n-2,dp);

    }

};
