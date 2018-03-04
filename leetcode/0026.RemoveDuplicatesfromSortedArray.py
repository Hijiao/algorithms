class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 2:
            if nums[0] == nums[1]:
                return 1
            else:
                return 2
        i, j = 0, len(nums) - 1
        max_moved = nums[j]
        min_moved = nums[i] - 1


l = [2, 2, 2, 3,4]
print l[:Solution().removeDuplicates(l)]
