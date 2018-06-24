class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast =nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        p = nums[0]
        slow = nums[slow]
        while p != slow:
            p =nums[p]
            slow = nums[slow]
        return p

print  Solution().findDuplicate([1,3,4,2,2])