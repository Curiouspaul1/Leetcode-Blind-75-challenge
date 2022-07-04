
from operator import index


def maxProfit(prices):
    result = 0
    left = 0
    for right in range(1, len(prices)):
            if prices[right] < prices[left]:
                left = right
            result = max(result, prices[right] - prices[left])
            
    return result

a =  [7,6,4,3,1]
print(maxProfit(a))