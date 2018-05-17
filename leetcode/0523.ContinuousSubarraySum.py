class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums)<2:
            return False

        if k == 0:
            indexs = []
            index = -1
            while True:
                try:
                    index = nums.index(0, index + 1)
                    indexs.append(index)
                except Exception:
                    break

            pre = -2
            combo = 1
            for i in range(len(indexs)):
                if pre + 1 == indexs[i]:
                    return True
                pre = indexs[i]
            return False

        sum_dict = {0:-1}
        s = 0

        for index,num in enumerate(nums):
            s = (s + num) % k
            if s in sum_dict:
                if index - sum_dict[s] > 1:
                    return True
            else:
                sum_dict[s] =index
        return False


