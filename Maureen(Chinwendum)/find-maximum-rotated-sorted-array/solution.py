class Solution:
    def findMin(self, nums: List[int]) -> int:        
        if len(nums)==1:
            return nums[0]
        
        if len(nums)==2:
            if nums[0]>nums[1]:
                return nums[1]
            else:
                return nums[0]
        
        mid=len(nums)//2
        
        if nums[mid] > nums[mid+1]:
            return nums[mid+1]
        
        right=self.findMin(nums[:mid+1])
        # if not right:
        #     right=-sys.maxsize
            
        left=self.findMin(nums[mid+1:])
        
        # if not left:
        #     left=-sys.maxsize
        
        if right >left :
            return left
        else:
           return right
            
        
     
        