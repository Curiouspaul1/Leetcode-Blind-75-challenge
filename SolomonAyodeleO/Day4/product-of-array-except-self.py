# Approach 1

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        answer = [] 
        for i in range(len(nums)):
            answer.append(prefix) #Add the prefix multiplication prefix to the answer
            prefix *= nums[i] # Then update the prefix
            
        # Do the reverse of prefix but multiply each postfix with the prefix in the array
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= postfix 
            postfix *= nums[i]
        #print(answer)
    
        return answer