class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [[0 for i in range(n + 1)] for i in range(n + 1)]
        f[1][1] = 1
        f[2][1] = 1
        for i in range(2, n+1):
            for j in range(2, i+1):
                f[i][j] = f[i - 1][j - 1] + f[i - 2][j - 1]
        return sum(f[n])


print Solution().climbStairs(2)
