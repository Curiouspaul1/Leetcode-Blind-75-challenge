class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l,r=0,1
        max_profit=0
        for x in range(len(prices)-1):
            if prices[r]>prices[l]:
                profit=prices[r]-prices[l]
                max_profit=max(max_profit, profit)
            else:
                l=r
            r=r+1
        return max_profit
                
        