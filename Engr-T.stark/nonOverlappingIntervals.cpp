class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        int numRemovals = 0;
        sort(intervals.begin(), intervals.end());
        vector<int> prev = intervals[0];
        for(int i = 1; i < intervals.size(); i++) {
            if(intervals[i][0] < prev[1]) {
              numRemovals += 1;
                prev[1] = min(intervals[i][1], prev[1]);
            } 
            else {
                prev[1] = intervals[i][1]; 
            }
        }
        return numRemovals;
    }
};
