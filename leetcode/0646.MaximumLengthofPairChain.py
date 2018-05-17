class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        # pairs.sort()
        # dp = [1] * len(pairs)
        # for i in xrange(len(pairs)):
        #     for j in xrange(i):
        #         if pairs[i][0] > pairs[j][1]:
        #             dp[i] =max(dp[i],dp[j]+1)
        # return max(dp)
        pairs.sort(key= lambda x:x[1])
        ans = 0
        cur = float('-inf')

        for first,second in pairs:
            if cur <first:
                ans+=1
                cur = second
        return ans
print Solution().findLongestChain([[1,2],[0,1],[4,8]])