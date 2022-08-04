class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal=len(nums)-1
        
        for y in range(len(nums)-1, -1, -1):
                if y+nums[y]>=goal:
                    goal=y
        if goal==0:
            return True
        else:
            return False
        
                
            
        