
# https://leetcode.com/problems/container-with-most-water/submissions/

class Solution:
    def maxArea(self, height):

        l, r = 0, len(height)-1
        ans = 0

        while l <= r:
            d = r-l
            ar = d * min(height[r], height[l])

            ans = max(ans, ar)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return ans
