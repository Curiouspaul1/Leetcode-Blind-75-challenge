class Solution {
 public:

set<string> set;

bool func(string s, int idx, vector<int>& dp)
{
    if(idx==s.size())
        return true;
    if(dp[idx]!=-1)
        return dp[idx];
    
    string str;
    
    for(int i=idx;i<s.size();i++)
    {
        str += s[i];
        if(set.find(str)!=set.end())
        {
            if(func(s,i+1,dp))
                return true;
        }
    }
    return dp[idx] = false;
}

bool wordBreak(string s, vector<string>& wordDict) {
    
    vector<int> dp(s.size(),-1);
    for(auto str: wordDict)
        set.insert(str);
    
    return func(s,0,dp);   
}
};
