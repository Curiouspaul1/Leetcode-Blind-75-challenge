import sys

class Solution:
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        cache = [0]*(amount+1)
        
        return self.actual_function(coins, amount, cache)

    def actual_function(self, coins, amount, cache):
        if amount==0:
            return 0

        if amount<0:
            return -1
        if cache[amount] != 0:
            return cache[amount]
        min=sys.maxsize
        for x in coins:
            check=self.actual_function(coins, amount-x, cache)
            if check<min and check != -1:
                min=1+check
            if min==sys.maxsize:
                cache[amount]=-1
            else:
                cache[amount]=min
        return cache[amount]