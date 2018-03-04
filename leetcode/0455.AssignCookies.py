class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        counter = 0
        g = sorted(g)
        s = sorted(s)
        # g.append(2**31)
        gi, si = 0, 0
        while (gi < len(g) and si < len(s)):
            if s[si] - g[gi] >= 0:
                gi += 1
            si += 1

        return gi


if __name__ == '__main__':
    g = [2, 3]
    s = [1, 2, 3]
    print Solution().findContentChildren(g, s)
