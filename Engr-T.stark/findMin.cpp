class Solution {
public:
    int findMin(vector<int>& nums) {
        sort(nums.begin(), nums.end(), [](int a, int b){ return a < b; });
        return nums[0];
    }
};
