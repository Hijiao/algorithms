class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start < end:
            n = (start + end) / 2
            if nums[n] > target:
                end = n - 1
            elif nums[n] < target:
                start = n + 1
            else:
                return n
        print start, end
        if nums[start] < target:
            return start + 1
        else:
            return start


l = [1, 3, 5, 6]
t = 7
Solution().searchInsert(l, t)
