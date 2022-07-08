class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        // vector<int> v;
        // for(int i = nums.size() - 1; i >= 0; --i) {
        //     v.push_back(accumulate(nums.begin(), nums.begin()+i, 0, plus<int>()));
        // }
        // for(int j = 0; j < nums.size(); j++) {
        //     cout << j << ", ";
        //     int currSum = accumulate(nums.begin() + j, nums.end(), 0, plus<int>());
        //     v[j] = max(v.at(j), currSum);
        // }
        // sort(v.begin(), v.end());
        // for(auto n: v) cout << n << ", ";
        // return v.back();
        int currMax = INT_MIN, maxEnd = 0;
  
        for (int i = 0; i < nums.size(); i++)
        {
            maxEnd = maxEnd + nums[i];
            if (currMax < maxEnd)
                currMax = maxEnd;

            if (maxEnd < 0)
                maxEnd = 0;
        }
        return currMax;

    }
};
