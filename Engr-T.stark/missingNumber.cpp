class Solution {
public:
    int missingNumber(vector<int>& nums) {
        if(nums.size() == 1) return nums[0] == 1 ? 0 : 1;
        sort(nums.begin(), nums.end(), [](int a, int b){ return a < b; });
        if(nums[0] != 0) return 0;
        for(int i = nums[0]; i < nums[nums.size() - 1]; i++) {
            if(nums[i+1] - nums[i] != 1) return ++nums[i];
        }
        return nums.size();
    }
};
