class Solution {
public:
    // void setZeroes(vector<vector<int>>& matrix) {
    //     int tempIndex = 0;
    //     // int step = matrix.size()
    //     for(int i = 0; i < matrix.size(); i++){
    //         for(int j = 0; j < matrix[i].size(); j++){
    //             if(matrix[i][j] == 0) {
    //                 tempIndex = j;
    //                 std::fill(matrix[i].begin(), matrix[i].end(), 0);
    //             }
    //         }
    //         for(int k = 0; k < matrix.size(); k++) {
    //             matrix[k][tempIndex] = 0;
    //         }
    //     }
    //     // return matrix;
    // }
    void setZeroes(vector<vector<int>>& matrix) {
        unordered_set<int>r;
        unordered_set<int>c;
        
        int row=matrix.size();
        int col=matrix[0].size();
        
        for(int i=0; i<row; i++){
            for (int j=0; j<col; j++){
                if(matrix[i][j]==0){
                    r.insert(i);
                    c.insert(j);
                }
            }
        }
        
       for (int i = 0; i < row; i++) {
          for (int j = 0; j < col; j++) {
            if (r.find(i)!=r.end() || c.find(j)!=c.end()) {
              matrix[i][j] = 0;
            }
          }
        }
    }
};
