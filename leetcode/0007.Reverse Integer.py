# https://leetcode.com/problems/reverse-integer
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        raw = ""
        for i in range(len(str(x)) - 1, 0, -1):
            raw = raw + str(x)[i]
        if str(x)[0] == '-':
            raw = "-" + raw
        else:
            raw += str(x)[0]
        r = int(raw)
        if r > 2147483647 or r < -2147483648:
            return 0
        return r

    def reverse1(self, x):
        s = (x > 0) - (x < 0)
        print(s)
        s = cmp(x, 0)
        print(x < 0)
        r = int(`s * x`[::-1])
        print(r)
        print(r < 2 ** 31)
        return s * r * (r < 2 ** 31)


if __name__ == '__main__':
    print(Solution().reverse1(2147483647))
    print 2 ** 31
