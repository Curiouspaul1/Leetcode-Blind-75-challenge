class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval)     {
        vector<vector<int>> ans;
        
        for(int i=0; i<intervals.size(); i++)
        {
            if(newInterval[1] < intervals[i][0])
            {
                ans.push_back(newInterval);
                newInterval = intervals[i];
            }
            else if(newInterval[0] > intervals[i][1])
            {
                ans.push_back(intervals[i]);
            }
            else if(newInterval[0] <= intervals[i][1] || newInterval[1] >= intervals[i][0])
            {
                newInterval[0] = min(intervals[i][0], newInterval[0]);
                newInterval[1] = max(intervals[i][1], newInterval[1]);
            }
        }
        
        ans.push_back(newInterval);
        
        return ans;
    }
};
