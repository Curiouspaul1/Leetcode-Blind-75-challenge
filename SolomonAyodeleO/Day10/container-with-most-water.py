# Approach 1 ==> Works but Timeout
class Solution:
    def maxArea(self, height: List[int]) -> int:
        currAmt = 0
        for i in range(len(height)):
            for j in range(i, len(height)):
                temp = (j-i) * min(height[i], height[j])
                if currAmt < temp:
                    currAmt = temp
        return currAmt


# Approach 2 ==> 
class Solution:
    def maxArea(self, height: List[int]) -> int:
        currAmt = 0
        i, j = 0, len(height)-1
        while i < j:
            temp = (j-i) * min(height[i], height[j])
            if currAmt < temp:
                currAmt = temp
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return currAmt