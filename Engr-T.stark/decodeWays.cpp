class Solution {
public:
    int numDecodings(string s) {

    vector<int> dp(s.size()+2, 0);

    dp[s.size()] = 1;

    for (int i = s.size()-1; i >= 0; --i) {

        dp[i] += dp[i+1];

        if(s[i] == '1')

            dp[i] += dp[i+2];

        else if(s[i] == '2' && i+1 < s.size() && s[i+1] < '7')

            dp[i] += dp[i+2];

        else if(s[i] == '0')

            dp[i] = 0;

    }

    return dp[0];

}
        

};
