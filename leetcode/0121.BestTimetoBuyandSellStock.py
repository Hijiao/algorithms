class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_buy_p = float("+inf")
        max_b = 0

        for p in prices:
            max_b = max(max_b, p - min_buy_p)
            min_buy_p = min(min_buy_p, p)
        return max_b



print Solution().maxProfit([3,3,5])
