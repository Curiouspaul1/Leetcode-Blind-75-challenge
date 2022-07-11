class Solution {

public:

    int search(vector<int>& nums, int target) {

        ///unordered_map<int, int> indices;

        //int j = 0;

        if(nums.size()==1 )

        { 

            if(nums[0]==target) return 0 ;

            else return -1;

        }

         for(int i=0;i<nums.size()/2;i++)

         {

             if(nums[i]==target){

                 return i;

             } 

         }

        

         for(int i=nums.size()-1;i>=nums.size()/2;i--)

         {

             if(nums[i]==target){ 

                 return i;

             }

         }

        

        return -1;

        

       // if(nums.size() == 1){

         //   if(nums[0] == target) return 0;

          //  else { return -1; }

        //}

        

       // for(int i = 0; i < nums.size()/2; i++) {

          //  if(nums[i] == target) return i;

        //}

        //for(int j = nums.size(); j >= nums.size()/2; --j){

        //    if(nums[j] == target) return j;

       // }

        

       // return -1;

        // for(auto n: nums) {

         //   indices[n] = j;

        //    cout << n << ": " << indices[n] << ", ";

          //  ++j;

     //   }

     //   sort(nums.begin(), nums.end(), [](int a, int b){ return a < b; });

     //  auto i = lower_bound(nums.begin(), nums.end(), target) - nums.begin();

    //   cout << i;

    //   return nums[i] == target ? indices[target] : -1;

        

        

    }

};
