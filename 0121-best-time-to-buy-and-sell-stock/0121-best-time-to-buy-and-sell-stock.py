class Solution:
    def maxProfit(self, prices):

        left = 0          # Buy Day
        right = 1         # Sell Day

        maxProfit = 0

        while right < len(prices):

            if prices[left] < prices[right]:

                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)

            else:
                left = right

            right += 1

        return maxProfit