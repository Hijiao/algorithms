class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        #         cset = set(s)
        #         diff_list =[]
        #         for c in cset:
        #             if s.count(c) != t.count(c):
        #                 diff_list.appendp(c)
        #         d = len(diff_list)

        #         for i in range(len(s)):
        #             if set(t[i:i+d])

        a = set(s)
        b = set(t)
        c = b - a
        d = len(t) - len(s)
        if len(c) == 0:
            for c in t:
                if s.count(c) != t.count(c):
                    return c

        for i in range(d - 1, len(t), 1):
            if set(t[i:i + d]) == c:
                return t[i:i + d]

print Solution().findTheDifference("a","aa")