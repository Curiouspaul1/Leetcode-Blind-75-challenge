class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount+1] *(amount+1)
        dp[0] =0
        for a in range(1, amount+1):
            for c in coins:
                if a-c >= 0:
                    dp[a] = min(dp[a],1+dp[a-c])
        if dp[amount] != (amount + 1):
            return dp[amount]
        else:
            return -1