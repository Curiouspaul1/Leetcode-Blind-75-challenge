class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        auto initSize = nums.size();
        sort(nums.begin(), nums.end());
        vector<int>::iterator last = unique(nums.begin(), nums.end());
        nums.resize(distance(nums.begin(), last));
        return initSize != nums.size();
    }
};

