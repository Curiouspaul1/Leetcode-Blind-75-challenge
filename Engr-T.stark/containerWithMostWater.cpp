class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0, right = height.size() - 1, curMax = 0, area;
        
        while(left < right)
        {
            area = min(height[left], height[right]) * (right - left);
            curMax = max(curMax, area);
            if(height[left] < height[right]) left++;
            else { right--; }
        }
        return curMax;
    }
};
