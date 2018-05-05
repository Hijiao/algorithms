class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return self.quick_sourt(nums, 0, len(nums) - 1)
        return reduce(lambda x, y: x ^ y, nums)

    def quick_sourt(self, nums, start, end):
        if end == start:
            return nums[start]
        i, j = start, end
        base = nums[i]
        exist = False
        while i < j:
            while i < j and nums[j] > base:
                j -= 1
            if nums[j] == base:
                exist = True
                j -= 1
                continue
            else:
                nums[i] = nums[j]
            while i < j and nums[i] < base:
                i += 1
            if nums[i] == base:
                exist = True
            nums[j] = nums[i]

        nums[i] = base

        print(nums[start:end])
        if i % 2 == 0:
            if exist is True:
                return self.quick_sourt(nums, i + 2, end)
            else:
                return nums[i]
        elif exist is True:
            return self.quick_sourt(nums, start, i - 1)
        else:
            return "-1"


print(Solution().singleNumber([-6, 12, 5, -6, 12, 4, -5, -5, 2, -3, 2, 4, 5, 16, -3, -4, 15, 15]))
