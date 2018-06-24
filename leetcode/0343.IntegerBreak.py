class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] * (n + 1)

        for i in xrange(2, n + 1):
            for j in xrange(1, i):
                dp[i] = max(dp[j] * (i - j), j * (i - j), dp[i])
                # print   "dp[%s] = max(dp[%s](%s) * %s,%s)" %(i,j,dp[j],  (i-j),dp[i])
        return dp[n]

print Solution().integerBreak(10)
