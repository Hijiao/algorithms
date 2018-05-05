class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        k_ = k
        frequent_dict = {}
        for num in nums:
            frequent_dict[num] = frequent_dict[num] + 1 if num in frequent_dict else 1

        uniqueWords = frequent_dict.keys()
        uniqueWords.sort()
        uniqueWords = sorted(uniqueWords, key=lambda x: frequent_dict[x], reverse=True)
        return uniqueWords[:k_]


print Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2)

