class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end(), [](int a, int b){ return a < b; });
        int left, right; // two pointers
        int sum = 0;
        vector<vector<int>> res;
        for(int i = 0; i < nums.size(); i++) {
            left = i + 1;
            right = nums.size() - 1;

            while(left < right)
            {
              if(nums[i] + nums[left] + nums[right] == sum) {                
                res.push_back({nums[i], nums[left], nums[right]});
                while(left != right && nums[left] == nums[left + 1]) left++;
                while(right != 0 && nums[right] == nums[right - 1]) right--;
                left++;
                right--;
              }
              else if(nums[i] + nums[left] + nums[right] < sum){ 
                left++;
              }
              else {
                right--;
              }
            }
        }
        sort(res.begin(), res.end());
        auto last = unique(res.begin(), res.end());
        res.resize(distance(res.begin(), last));
        return res;
        
        // --- a solution I found --- prefer mine sha //
        // vector<vector<int>> ans;
        // sort(nums.begin(),nums.end());
        // int n=nums.size();
        // for(int i=0;i<n; i++)
        // {
        //     int j=i+1,k=n-1;//two pointers
        //     while(j<n && j<k)
        //     {
        //         if(nums[j]+nums[k] == -nums[i])
        //         {
        //             ans.push_back({nums[i],nums[j],nums[k]});
        //             while(k!=0 && nums[k]==nums[k-1]) k--;//to avoid duplicates 
        //             while(j!=n-1 && nums[j]==nums[j+1]) j++;
        //             j++,k--;
        //         }
        //         else if(nums[j]+nums[k] > -nums[i]) 
        //         {
        //             while(k!=0 && nums[k]==nums[k-1]) k--;
        //             k--;
        //         }
        //         else
        //         {
        //             while(j!=n-1 && nums[j]==nums[j+1]) j++;
        //             j++;
        //         }
        //     }
        //     while(i!=n-1 && nums[i]==nums[i+1]) i++;
        // }
        // for(auto triplet : ans)
        //     sort(triplet.begin(),triplet.end());
        // return ans;
    }
};
