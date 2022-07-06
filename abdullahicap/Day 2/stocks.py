def maxProfit(self, prices):
        mi = prices[0]
        ma = max(prices)
        max_profit = 0

        for price in prices:
            mi = min(price, mi)
            max_profit = max(price - mi, max_profit)

        return max_profit