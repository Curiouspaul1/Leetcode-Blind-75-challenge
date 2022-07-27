class Solution {
public:
    int rob(vector<int>& nums) {
        int len = nums.size();
        if(len == 0) return 0;
        if(len == 1) return nums[0];
        
        vector<int> house(len, 0);
        house[0] = nums[0];
        house[1] = max(nums[0],nums[1]);
            
        for (int i = 2; i < len; i++) {
            house[i] = max(nums[i] + house[i - 2], house[i - 1]);
        }
        return house[len - 1];
    }
};
