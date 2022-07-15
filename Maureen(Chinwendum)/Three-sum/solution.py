class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        x=0
        result=[]
        y=0
        nums.sort()
        print(nums)
        while y <= len(nums)-3:
                if y>0 and nums[y]==nums[y-1]:
                    y=y+1
                    continue
                l,r=y+1,len(nums)-1
                while l<r:
                    if r<len(nums)-1 and l>y+1 and nums[l]==nums[l-1] and nums[r]==nums[r+1] :
                        l=l+1
                        continue                       
                    if -(nums[l]+nums[r])>nums[y]:
                        l=l+1
                    elif -(nums[l]+nums[r])<nums[y]:
                        r=r-1
                    elif -(nums[l]+nums[r])==nums[y]:
                        result.append([nums[y],nums[l],nums[r]])
                        r=r-1
                        l=l+1       
                y=y+1
        return result
                    
                    
                
                