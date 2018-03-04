# https://leetcode.com/problems/two-sum/description/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for i in range(len(nums)):
            d = target - nums[i]
            if nums_dict.get(d) is not None:
                return [i, nums_dict.get(d)]
            nums_dict.update({nums[i]: i})


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([3, 3], 6))
