# Arvin's approach.
# Time --> O(n)
# Space --> O(1)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0

        for i in range(1,len(prices)):
            profit = prices[i] - prices[i-1]
            if profit > 0:
                maxProfit = maxProfit + profit
 
        return maxProfit

        