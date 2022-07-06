class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res = 0
        left, right = 0, 1
        
        while right <= len(prices) - 1:
            if prices[right] < prices[left]:
                left = right
            else:
                profit = prices[right] - prices[left]
                res = max(profit, res)
                
            right += 1
        
        return res