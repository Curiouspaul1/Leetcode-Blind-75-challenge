class Solution {
public:
    int maxProduct(vector<int>& nums) {
      if (!nums.size()) return 0;
        int result = nums[0];
        int maxProd = result, minProd = result;
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] < 0) {
                swap(maxProd, minProd);
            }
            maxProd = max(nums[i], nums[i] * maxProd);
            minProd = min(nums[i], nums[i] * minProd);
            result = max(maxProd, result);
        }
        return result;
   }
};
