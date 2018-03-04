class Solution(object):
    def removeElementFirst(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 1:
            if nums[0] == val:
                return 0
            else:
                return 1
        if len(nums) == 0:
            return 0
        i, j = 0, len(nums) - 1
        while i <= j:
            while (i < j) and nums[i] != val:
                i += 1
            while (i < j) and nums[j] == val:
                j -= 1
            if i == j:
                if nums[i] == val:
                    return i
                else:
                    return i + 1
            nums[i] = nums[j]
            i += 1
            j -= 1
        return i

    def removeElement(self, nums, val):
        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[i] == val:
                nums[i] = nums[j]
                j -= 1
            else:
                i += 1
        return i

m = [3, 2, 2, 3]
print Solution().removeElement(m, 3)
print m
