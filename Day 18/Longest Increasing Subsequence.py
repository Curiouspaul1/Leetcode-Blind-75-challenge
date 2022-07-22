from ast import List
from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [nums[0]]
        
        for num in nums[1:]:
            if lis and num > lis[-1]:
                lis.append(num)
            else:
                index = bisect_left(lis, num)
                lis[index] = num
                
        return len(lis)
        
        
        
        
        
        # class Solution:
    # def lengthOfLIS(self, nums: List[int]) -> int:  # Time: O(n*n) and Space: O(n)

    #     LIS = [1] * len(nums)  # in LIS we will store the longest increasing subsequence from that index to the last index

    #     for i in range(len(nums) - 1, -1, -1):        # staring from the last index, cause LIS[last] = 1 is the base case 
    #         for j in range(i + 1, len(nums)):         # staring from the last+1 index, will run for nums-1 times
    #             if nums[i] < nums[j]:                 # if i < i+1 satisfies the LIS condition 
    #                 LIS[i] = max(LIS[i], 1 + LIS[j])  # then choose the max from i or 1(where 1 indicates i index) + i+1 
					
    #     return max(LIS)  