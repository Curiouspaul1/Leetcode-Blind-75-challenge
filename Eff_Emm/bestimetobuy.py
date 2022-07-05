class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mins = prices[0]
        max_profit = 0
        
        maxs = 0
        for i in range(len(prices)):
            if prices[i] < mins:
                mins = prices[i]
            elif prices[i] - mins > max_profit:
                max_profit = prices[i] - mins
      
        
        return max_profit
            
        
new = Solution()
print(new.maxProfit([1,4,5,7]))