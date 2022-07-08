int prodExcept(vector<int>, int);
class Solution {
public:    
    // vector<int> productExceptSelf(vector<int>& nums) {
    //     vector<int> answer;
    //     int i = 0;
    //     while(i < nums.size())
    //     {
    //         answer.push_back(prodExcept(nums, i));
    //         i++;
    //     }
    //     return answer;
    // }
    // int prodExcept(vector<int> v, int n) {
    //     if(v[n] == 0) v[n] = 1;
    //     int res = std::accumulate(v.begin(), v.end(), 1, [](int x, int y){ return x * y; });
    //     return res/v[n];
    // }
    vector<int> productExceptSelf(vector<int>& nums) {
      vector<int> left(nums.size(), 1);
      vector<int> right(nums.size(), 1);
      for(int i=1; i<nums.size(); i++){
          left[i] = left[i-1]*nums[i-1];
      }
      for(int i= nums.size()-2; i>=0; i--){
          right[i] = right[i+1]*nums[i+1];
      } 
      vector<int> output(nums.size());
      for(int i=0; i<nums.size(); i++){
          output[i] = left[i]*right[i];
      }
        return output;
    }
};
