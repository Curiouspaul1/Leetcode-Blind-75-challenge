
# https://leetcode.com/problems/longest-increasing-subsequence/submissions/

class Solution:
    def lengthOfLIS(self, nums):
        new=[]
        n=0
        for i in nums:
            idx=self.binSearch(new,i)
            if idx>=n:
                if n==0 or new[-1]!=i:
                    new.append(i)
                    n+=1
            else:
                if idx==0 or new[idx-1]!=i:new[idx]=i
        return len(new)
        
    def binSearch(self,nums,val):
        low,high=0,len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==val and mid<high and nums[mid+1]>val:return mid+1
            if nums[mid]<=val:low=mid+1
            else:high=mid-1
        return low
 
        
        