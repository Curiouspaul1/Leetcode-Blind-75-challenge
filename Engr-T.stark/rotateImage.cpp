class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int temp = 0;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < i; j++) {
                cout<< j;
                temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        // swap columns to have 90 deg rotation
        double m = floor(double(n/2));
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++) {
                temp = matrix[i][j];
                matrix[i][j] = matrix[i][n - j - 1];
                matrix[i][n - j - 1] = temp;
            }
        }
        // return matrix;
    }
};
