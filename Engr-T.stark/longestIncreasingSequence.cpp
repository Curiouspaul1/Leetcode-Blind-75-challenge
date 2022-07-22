class Solution {
public:
int f(int ind,int prev_ind,int n,vector<int>&arr,vector<vector<int>>&dp)
{
    // Base Case
    if(ind==n) return 0;
    if(dp[ind][prev_ind+1]!=-1) return dp[ind][prev_ind+1];
    int len = f(ind+1,prev_ind,n,arr,dp); // not take 
    if(prev_ind==-1 || arr[ind]>arr[prev_ind])  //take 
    len = max(len,1+f(ind+1,ind,n,arr,dp));
    return dp[ind][prev_ind+1]=len;
}
    int lengthOfLIS(vector<int>& nums) {
     int n = nums.size();
    vector<vector<int>>dp(n,vector<int>(n+1,-1));
    return f(0,-1,n,nums,dp);
    }
};
