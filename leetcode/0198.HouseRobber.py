class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for n in nums:
            last,now = now,max(last +n,now)
        return now

print Solution().rob([5,1,1,5])