class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum_dict = {0:1}
        s = 0
        total = 0
        for num in nums:
            s = (s + num)
            total += sum_dict.get(s-k,0)
            sum_dict[s] = sum_dict.get(s, 0) + 1

        return total


print  Solution().subarraySum([-1,-1,1], 0)
