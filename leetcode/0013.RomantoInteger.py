# https://leetcode.com/problems/roman-to-integer
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {
            "I": 1,
            "X": 10,
            "C": 100,
            "M": 1000,
            "V": 5,
            "L": 50,
            "D": 500,
        }
        t = 0
        for i in range(len(s) - 1):
            if d.get(s[i]) < d.get(s[i + 1]):
                t = t - d.get(s[i])
            else:
                t = t + d.get(s[i])
        t = t + d.get(s[-1])

        print(t)

        return t


if __name__ == '__main__':
    print(Solution().romanToInt("DCXXI"))
    print(Solution().romanToInt("MCMLXXX"))
