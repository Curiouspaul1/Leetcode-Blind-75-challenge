class Solution:
    def search(self, nums, target):
        try:
            return (nums.index(target))
        except:
            return -1
    
numList = [4,5,6,7,0,1,2]
target = 0
print(Solution().search(numList))
