class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        max_amount = -1
        change = False
        compute = lambda start, end: min(height[start], height[end]) * (end - start)
        while start < end:
            amount = compute(start, end)

            if amount > max_amount:
                max_amount = amount

            if height[start] < height[end]:
                start += 1
            elif height[start] > height[end]:
                end -= 1
            else:
                if (height[start + 1] - height[start]) > (height[end - 1] - height[end]):
                    start += 1
                else :
                    end -= 1                
        return max_amount
        
