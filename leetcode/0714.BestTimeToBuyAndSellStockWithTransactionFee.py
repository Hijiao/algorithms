class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        cash = [0] * len(prices)
        hold = [0] * len(prices)

        hold[0] = -prices[0]

        for i in range(1, len(prices)):
            cash[i] = max(cash[i - 1], prices[i] + hold[i - 1] - fee)
            hold[i] = max(hold[i - 1], cash[i - 1] - prices[i])

        return cash[-1]


print Solution().maxProfit([1, 3, 2, 8, 4, 9], 2)
