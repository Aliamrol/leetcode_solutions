class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < buy_price:
                buy_price = prices[i]
            if max_profit < prices[i] - buy_price:
                max_profit = prices[i] - buy_price
        return max_profit


#%% Arvin's approach is as like as Ali's approach with a bit difference in for loop. Also, defining
# a variable with float number is better that getting the first element of an array in time.
# Time --> O(n)
# Space --> O(1)

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1631695191/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        minPrice = float('inf')
        for price in prices:
            if price < minPrice:
                minPrice = price
            profit = price - minPrice
            if profit > maxProfit:
                maxProfit = profit
        return maxProfit