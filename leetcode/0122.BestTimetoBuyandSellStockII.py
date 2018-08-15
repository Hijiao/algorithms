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



    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        hold = float("-inf")
        not_hold = 0

        for p in prices:
            hold = max(hold, not_hold - p)
            not_hold = max(not_hold, hold + p)

        return not_hold