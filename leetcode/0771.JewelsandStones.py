class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        Jset = set(J)
        return sum(x in Jset for x in S)


print Solution().numJewelsInStones("asd", "sadd")
