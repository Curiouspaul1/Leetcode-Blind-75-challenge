class Solution {
public:
    int missingNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end(), [](int a, int b){ return a < b; });
        if(nums[0] != 0) return 0;
        for(int i = nums[0]; i < nums[nums.size() - 1]; i++) {
            if(nums[i+1] - nums[i] != 1) return ++nums[i];
        }
        return nums.size();
    }
};

//         int n = nums.size();
// 		   int total = n*(n+1) / 2;
        
//         for(int i=0; i<nums.size(); i++) {
//             total -= nums[i];
//         }
//         return total;

//         return nums.size() * (nums.size() + 1) / 2 - accumulate(nums.begin(), nums.end(), 0); --> one liner

//  <<<<<<<<< ------ Bit Manipulation ------ >>>>>>>
//         int result = nums.size(); // initialize result to size of vector
//         int i=0; // initialize i to 0
//         for(int num:nums){ // for each number in vector
//             result ^= num; // XOR result with number
//             result ^= i; // XOR result with i
//             i++; // increment i
//         }
//         return result; // return result that is the missing number
