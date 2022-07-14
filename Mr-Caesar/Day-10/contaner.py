class Solution:
    def maxArea(self, height: List[int]) -> int:
        x, y = 0, len(height) - 1
        res = 0

        while x < y:
            area = (y-x) * min(height[x], height[y])
            res = max(res, area)

            if height[x] <= height[y]:
                x += 1
            elif height[x] > height[y]:
                y -= 1
            else:
                y -= 1
        return res
