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
