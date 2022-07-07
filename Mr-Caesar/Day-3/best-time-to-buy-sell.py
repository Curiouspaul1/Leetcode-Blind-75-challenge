class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, max_profit = 0,1,0
        
        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            if prices[sell] < prices[buy]:
                buy = sell
            max_profit = max(max_profit, profit)
            
            sell+=1
            
        return max_profit            