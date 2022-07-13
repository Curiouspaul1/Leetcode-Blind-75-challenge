# Approcach 1

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = max(prices)
        profit = 0
        
        for i in range(len(prices)):
            if minPrice > prices[i]:
                minPrice =  prices[i]
            if prices[i] - minPrice > profit:
                profit =  prices[i] - minPrice
        return profit
                
# Runtime: 1000 ms, faster than 97.12% of Python3 online submissions for Best Time to Buy and Sell #Stock.
#Memory Usage: 25.1 MB, less than 38.07% of Python3 online submissions for Best Time to Buy and Sell #Stock.


# Approach 2

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = sys.maxsize
        profit = 0
        
        for i in prices:
            if i <= minPrice:
                minPrice = i
            elif profit < (i - minPrice):
                profit = i - minPrice
        
        return profit