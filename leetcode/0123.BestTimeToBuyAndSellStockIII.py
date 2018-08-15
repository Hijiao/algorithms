class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        self.prices = prices
        l = len(prices)
        if l < 2:
            return 0
        max_p = 0
        max_p = max(max_p, self.maxProfitOnece(0, l))
        for i in range(1, l - 1):
            # if prices[i] > prices[i - 1] and prices[i] > prices[i + 1]:
            #     max_p = max(max_p, self.maxProfitOnece(0, i) + self.maxProfitOnece(i, l))
            if prices[i] < prices[i - 1] and prices[i] <= prices[i + 1]:
                max_p = max(max_p, self.maxProfitOnece(0, i) + self.maxProfitOnece(i, l))

        return max_p

    def maxProfitOnece(self, start, end):
        """
        :type prices: List[int]
        :rtype: int
        """

        min_buy_p = float("+inf")
        max_b = 0
        for i in range(start, end):
            p = self.prices[i]
            if p < min_buy_p:
                min_buy_p = p
            else:
                max_b = max(max_b, p - min_buy_p)
        print start, end, max_b

        return max_b


print Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4])
# print Solution().maxProfitOnece([3, 3, 5])
