class Solution {

public:

    vector<vector<int>> dp;

int uniquePathsUtil(int m, int n) {

    if(m == 1 || n == 1) return 1;

    if(dp[m][n] != -1)

        return dp[m][n];

    return dp[m][n] = uniquePathsUtil(m-1, n) + uniquePathsUtil(m, n-1);

}

int uniquePaths(int m, int n) {

    dp.clear();

    dp.assign(m+1, vector<int>(n+1, -1));

    return uniquePathsUtil(m, n);

}

};
