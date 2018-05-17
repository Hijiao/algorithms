class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <=0:
            return 0
        if n > 10:
            n=10
        dp = [1] * (n+1)
        dp[1] = 10
        for i in range(2,n+1):
            dp[i] = dp[i-1] + self.countdown(i)
        return dp[n]

    def countdown(self,count):
        ret = 9
        for i in range(9,10-count,-1):
            ret *=i
        return ret

print Solution().countNumbersWithUniqueDigits(2)