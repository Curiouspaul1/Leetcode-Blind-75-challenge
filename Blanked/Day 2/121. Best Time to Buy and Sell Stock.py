
# https://leetcode.com/submissions/detail/671845804/
class Solution(object):
    def maxProfit(self, prices):
        index=0
        ret=0
        for i in range(1,len(prices)):
            tempret=prices[i]-prices[index]
            if tempret<0:
                index=i
            if tempret>0 and tempret>ret:
                ret=tempret
        return ret
