class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        best_profits = [0]
        prev = 0
        curr = 1
        
        while curr < len(prices):
            if prices[curr] > prices[prev]:
                best_profits.append(prices[curr] - prices[prev])
            else:
                prev = curr
            curr += 1
        return max(best_profits)
        
