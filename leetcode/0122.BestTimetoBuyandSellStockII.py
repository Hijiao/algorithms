# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(1, len(prices)):
            d = prices[i] - prices[i - 1]
            if d > 0:
                profit += d
        return profit
